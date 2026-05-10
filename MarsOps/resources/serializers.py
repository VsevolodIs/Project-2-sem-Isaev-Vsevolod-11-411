from rest_framework import serializers
from .models import Category, Resources


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ResourceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=Category.objects.all(), write_only=True)

    class Meta:
        model = Resources
        fields = ['id', 'title', 'description', 'price', 'stock', 'is_available', 'category', 'category_id']