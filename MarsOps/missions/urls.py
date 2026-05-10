from django.urls import path, include
from . import views, api_views

app_name = 'missions'

urlpatterns = [
    path('', views.mission_list, name='mission_list'),
    path('api/missions/', api_views.MissionListAPIView.as_view(), name='api_mission'),
    path('api/missions/<int:pk>', api_views.MissionDetailAPIView.as_view(), name='api_mission_detail'),
]