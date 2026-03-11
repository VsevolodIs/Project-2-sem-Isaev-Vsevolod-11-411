from django.shortcuts import render
from stations.models import Station


def station_list(request):
    stations = Station.objects.all()
    return render(request, 'stations/station_list.html', {
        'stations': stations
    })