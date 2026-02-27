from django.shortcuts import render

MOCK_HABITATS = [
    {'name': 'Жилой модуль A', 'capacity': 6, 'in_stock': True},
    {'name': 'Жилой модуль B', 'capacity': 4, 'in_stock': True},
    {'name': 'Научный модуль', 'capacity': 3, 'in_stock': True},
    {'name': 'Медицинский модуль', 'capacity': 2, 'in_stock': True},
    {'name': 'Складской модуль', 'capacity': 0, 'in_stock': False},
]

def habitat_list(request):
    context = {'habitats': MOCK_HABITATS}
    return render(request, 'habitat/habitat_list.html', context)