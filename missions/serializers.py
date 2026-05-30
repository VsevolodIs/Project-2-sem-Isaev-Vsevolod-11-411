from rest_framework import serializers
from .models import Mission


class MissionSerializer(serializers.ModelSerializer):
    station_name = serializers.CharField(source='station.name', read_only=True)
    crew_count = serializers.IntegerField(source='crew_members.count', read_only=True)

    class Meta:
        model = Mission
        fields = ['id', 'name', 'mission_type', 'station', 'station_name', 'status', 'objective', 'crew_members',
                  'crew_count']