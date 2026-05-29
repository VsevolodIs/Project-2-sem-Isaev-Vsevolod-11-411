from rest_framework import generics
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAdminUser
from resources.models import Category, Resources
from resources.serializers import CategorySerializer, ResourceSerializer


@extend_schema(
    summary="Список категорий",
    description="Возвращает массив всех категорий ресурсов",
    tags=['Ресурсы']
)
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(
    summary="Список ресурсов",
    description="Возвращает массив всех ресурсов",
    tags=['Ресурсы']
)
class ResourceListAPIView(generics.ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer


@extend_schema(
    summary="Детальная информация о ресурсе",
    description="Возвращает полную информацию о ресурсе по id",
    tags=['Ресурсы']
)
class ResourceDetailAPIView(generics.RetrieveAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer


@extend_schema(
    summary="Создать ресурс (Только для админов)",
    description="Создает новый ресурс в каталоге",
    tags=['Ресурсы']
)
class ResourceCreateAPIView(generics.CreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminUser]