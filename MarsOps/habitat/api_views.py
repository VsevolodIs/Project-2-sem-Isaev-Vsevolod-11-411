from rest_framework import generics
from drf_spectacular.utils import extend_schema
from habitat.models import Habitat
from habitat.serializers import HabitatSerializer


@extend_schema(
    summary="Список модулей",
    description="Возвращает массив всех жилых модулей",
    tags=['Модули']
)
class HabitatListAPIView(generics.ListAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer


@extend_schema(
    summary="Детальная информация о модуле",
    description="Возвращает полную информацию о модуле по id",
    tags=['Модули']
)
class HabitatDetailAPIView(generics.RetrieveAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer