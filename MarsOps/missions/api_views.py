from rest_framework import generics
from drf_spectacular.utils import extend_schema
from missions.models import Mission
from missions.serializers import MissionSerializer


@extend_schema(
    summary="Список миссий",
    description="Возвращает массив всех миссий",
    tags=['Миссии']
)
class MissionListAPIView(generics.ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


@extend_schema(
    summary="Детальная информация о миссии",
    description="Возвращает полную информацию о миссии по id",
    tags=['Миссии']
)
class MissionDetailAPIView(generics.RetrieveAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer