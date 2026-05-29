from rest_framework import generics
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAdminUser
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

@extend_schema(
    summary="Создать модуль (Только для админов)",
    description="Создает новый модуль в каталоге",
    tags=['Модули']
)
class HabitatCreateAPIView(generics.CreateAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer
    permission_classes = [IsAdminUser]