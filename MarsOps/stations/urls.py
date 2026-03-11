from django.urls import path, include
from . import views

app_name = 'stations'

urlpatterns = [
    path('', views.station_list, name='station_list'),
]