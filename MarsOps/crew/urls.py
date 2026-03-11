from django.urls import path, include
from . import views

app_name = 'crew'

urlpatterns = [
    path('', views.crew_members, name='crew_members'),
]