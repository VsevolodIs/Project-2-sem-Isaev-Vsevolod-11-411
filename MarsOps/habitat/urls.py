from django.urls import path, include
from . import views

app_name = 'habitat'

urlpatterns = [
    path('', views.habitat_list, name='habitat_list'),
]