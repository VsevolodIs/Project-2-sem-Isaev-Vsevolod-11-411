from django.urls import path, include
from . import views, api_views

app_name = 'resources'

urlpatterns = [
    path('resources/', views.resources_list, name='resources_list'),
    path('api/categories/', api_views.CategoryListAPIView.as_view(), name='api_categories'),
    path('api/resources/', api_views.ResourceListAPIView.as_view(), name='api_resources'),
    path('api/resources/<int:pk>', api_views.ResourceDetailAPIView.as_view(), name='api_resources_detail'),
    path('api/cars/create/', api_views.ResourcesCreateAPIView.as_view(), name='api_resources_create'),
]