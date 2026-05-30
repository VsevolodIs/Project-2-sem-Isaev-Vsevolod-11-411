from django.urls import path, include
from .views import station_list, station_detail, add_station_review, edit_station_review, delete_station_review, \
    toggle_favorite, favorites_list, toggle_theme
from . import api_views, views

app_name = 'stations'

urlpatterns = [
    path('', station_list, name='station_list'),
    path('<int:station_id>/', station_detail, name='station_detail'),
    path('<int:station_id>/add-review/', add_station_review, name='add_review'),
    path('review/<int:review_id>/edit/', edit_station_review, name='edit_review'),
    path('<int:review_id>/delete/', delete_station_review, name='delete_review'),
    path('toggle-theme/', toggle_theme, name='toggle_theme'),
    path('favorites/', favorites_list, name='favorites'),
    path('<int:station_id>/toggle-favorite/', toggle_favorite, name='toggle_favorite'),
    path('api/stations', api_views.StationListAPIView.as_view(), name='api_stations'),
    path('api/stations/<int:pk>', api_views.StationDetailAPIView.as_view(), name='api_station_detail'),
    path('api/station-reviews', api_views.StationReviewListAPIView.as_view(), name='api_station_reviews'),
    path('api/station/create/', api_views.StationCreateAPIView.as_view(), name='api_station_create'),
    path('api/station-reviews/create/', api_views.StationReviewCreateAPIView.as_view(), name='api_review_create'),
    path('api/station-reviews/<int:pk>/delete/', api_views.StationReviewDestroyAPIView.as_view(), name='api_review_destroy'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
]