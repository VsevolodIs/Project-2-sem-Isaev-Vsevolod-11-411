from django.shortcuts import render
from habitat.models import Habitat


def habitat_list(request):
    habitats = Habitat.objects.all()
    return render(request, 'habitat/habitat_list.html', {
        'habitats': habitats
    })