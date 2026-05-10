from rest_framework import serializers
from .models import CrewMember, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'telegram']


class CrewMemberSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    assigned_station_name = serializers.CharField(source='assigned_station.name', read_only=True)

    class Meta:
        model = CrewMember
        fields = ['id', 'user', 'name', 'role', 'status', 'assigned_station', 'assigned_station_name', 'profile']