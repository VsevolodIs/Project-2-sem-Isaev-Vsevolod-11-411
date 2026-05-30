from rest_framework import serializers
from .models import Habitat

class HabitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitat
        fields = ['id', 'name', 'capacity', 'in_stock']