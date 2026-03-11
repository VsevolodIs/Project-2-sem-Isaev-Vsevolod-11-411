from django.shortcuts import render
from .models import Resources, Category


def resources_list(request):
    resources_db = Resources.objects.all()
    categories_db = Category.objects.all()

    context = {
        'resources': resources_db,
        'categories': categories_db
    }
    return render(request, 'resources/resources_list.html', context)