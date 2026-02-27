from django.shortcuts import render

MOCK_RESOURCES = [
    {'name': 'Кислород', 'quantity': 500, 'unit': 'л', 'in_stock': True},
    {'name': 'Вода', 'quantity': 1200, 'unit': 'л', 'in_stock': True},
    {'name': 'Пища (сублиматы)', 'quantity': 300, 'unit': 'кг', 'in_stock': True},
    {'name': 'Солнечные батареи', 'quantity': 0, 'unit': 'шт', 'in_stock': False},
    {'name': 'Запчасти для ровера', 'quantity': 0, 'unit': 'шт', 'in_stock': False},
]

def resources_list(request):
    context = {'resources': MOCK_RESOURCES}
    return render(request, 'resources/resources_list.html', context)