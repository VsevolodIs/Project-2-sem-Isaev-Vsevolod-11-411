from django.shortcuts import render, redirect
from crew.models import CrewMember
from .forms import CustomRegisterForm, ProfileForm
from .models import Profile
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from stations.models import StationReview


def crew_members(request):
    crews = CrewMember.objects.all()
    return render(request, 'crew/crew_members.html', {
        'crews': crews
    })

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)
            login(request, user)
            return redirect('crew:profile')
    else:
        form = CustomRegisterForm()
    return render(request, 'crew/register.html', {'form': form})

@login_required
def profile_view(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('crew:profile')
    else:
        form = ProfileForm(instance=user_profile)

    user_reviews = StationReview.objects.filter(author=request.user)

    context = {
        'profile': user_profile,
        'reviews': user_reviews,
        'form': form
    }

    return render(request, 'crew/profile.html', context)