from django.urls import path, include
from . import views

app_name = 'missions'

urlpatterns = [
    path('', views.mission_list, name='mission_list'),
]