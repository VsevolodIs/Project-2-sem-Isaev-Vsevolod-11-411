from rest_framework import serializers
from .models import Station, StationReview


class StationReviewSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = StationReview
        fields = ['id', 'station', 'author', 'author_name', 'rating', 'text',]


class StationSerializer(serializers.ModelSerializer):
    reviews = StationReviewSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    reviews_count = serializers.IntegerField(source='reviews.count', read_only=True)

    class Meta:
        model = Station
        fields = ['id', 'name', 'station_type', 'established_date', 'crew_capacity',
                  'reviews', 'average_rating', 'reviews_count']