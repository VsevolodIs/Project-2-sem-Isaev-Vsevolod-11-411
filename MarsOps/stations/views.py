from django.shortcuts import render, get_object_or_404, redirect
from pyexpat.errors import messages
from stations.models import Station
from stations.forms import StationReviewForm
from django.contrib.auth.decorators import login_required
from .models import StationReview
from django.http import HttpResponseRedirect


def station_list(request):
    stations = Station.objects.all()

    favorites = [int(f) for f in request.session.get('favorites', [])]

    request.session['total_visits'] = request.session.get('total_visits', 0) + 1

    viewed_ids = request.session.get('viewed_stations', [])
    recent_stations = Station.objects.filter(id__in=viewed_ids) if viewed_ids else []

    sort_by = request.COOKIES.get('sort_stations', 'name')

    if sort_by == 'name':
        stations = stations.order_by('name')
    elif sort_by == 'date':
        stations = stations.order_by('-established_date')

    context = {
        'stations': stations,
        'favorites': favorites,
        'recent_stations': recent_stations,
        'total_visits': request.session.get('total_visits', 0),
    }

    response = render(request, 'stations/station_list.html', context)

    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'

    return response


def station_detail(request, station_id):
    station = get_object_or_404(Station, id=station_id)

    viewed = request.session.get('viewed_stations', [])
    if station_id not in viewed:
        viewed.insert(0, station_id)
        request.session['viewed_stations'] = viewed[:5]

    view_count = request.session.get(f'station_{station_id}_views', 0) + 1
    request.session[f'station_{station_id}_views'] = view_count

    recommendations = Station.objects.filter(
        station_type=station.station_type
    ).exclude(id=station_id)[:3]

    favorites = [int(f) for f in request.session.get('favorites', [])]

    context = {
        'station': station,
        'reviews': station.reviews.all(),
        'form': StationReviewForm(),
        'view_count': view_count,
        'recommendations': recommendations,
        'favorites': favorites,
    }

    response = render(request, 'stations/station_detail.html', context)

    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'

    return response

@login_required
def add_station_review(request, station_id):
    station = get_object_or_404(Station, id=station_id)

    if request.method == 'POST':
        form = StationReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.station = station
            new_review.author = request.user
            new_review.save()

    return redirect('stations:station_detail', station_id=station.id)

@login_required
def edit_station_review(request, review_id):
    review = get_object_or_404(StationReview, id=review_id, author=request.user)

    if request.method == 'POST':
        form = StationReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('stations:station_detail', station_id=review.station.id)

    else:
        form = StationReviewForm(instance=review)

    return render(request, 'stations/review_edit.html', {'form': form, 'review': review})

@login_required
def delete_station_review(request, review_id):
    review = get_object_or_404(StationReview, id=review_id, author=request.user)
    station_id = review.station.id

    if request.method == 'POST':
        review.delete()
        return redirect('stations:station_detail', station_id=station_id)

    return render(request, 'stations/confirm_delete.html', {'review': review})


def toggle_theme(request):
    current = request.COOKIES.get('theme', 'light')
    new = 'dark' if current == 'light' else 'light'

    resp = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


    resp.set_cookie('theme', new, max_age=60 * 60 * 24 * 30, samesite='Lax')

    return resp

def favorites_list(request):
    favorites_ids = request.session.get('favorites', [])
    favorites_stations = Station.objects.filter(id__in=favorites_ids)

    context = {
        'favorites': favorites_stations,
        'favorites_count': len(favorites_ids),
    }
    return render(request, 'stations/favorites.html', context)


@login_required
def toggle_favorite(request, station_id):
    favorites = [int(f) for f in request.session.get('favorites', [])]

    if station_id in favorites:
        favorites.remove(station_id)
    else:
        favorites.append(station_id)

    request.session['favorites'] = favorites
    request.session.modified = True

    return redirect(request.META.get('HTTP_REFERER', '/'))