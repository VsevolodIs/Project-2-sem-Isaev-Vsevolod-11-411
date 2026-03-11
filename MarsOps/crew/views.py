from django.shortcuts import render
from crew.models import CrewMember


def crew_members(request):
    crews = CrewMember.objects.all()
    return render(request, 'crew/crew_members.html', {
        'crews': crews
    })