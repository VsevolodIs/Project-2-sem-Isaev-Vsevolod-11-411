from django.urls import path, include
from . import views, api_views

app_name = 'habitat'

urlpatterns = [
    path('', views.habitat_list, name='habitat_list'),
    path('api/habitat/', api_views.HabitatListAPIView.as_view(), name='api_habitat'),
    path('api/habitat/<int:pk>', api_views.HabitatDetailAPIView.as_view(), name='api_habitat_detail'),
]