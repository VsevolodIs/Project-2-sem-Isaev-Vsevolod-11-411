from django.shortcuts import render
from missions.models import Mission


def mission_list(request):
    missions = Mission.objects.all()
    return render(request, 'missions/mission_list.html', {
        'missions': missions
    })

