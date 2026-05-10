from rest_framework import generics
from drf_spectacular.utils import extend_schema
from stations.models import Station, StationReview
from stations.serializers import StationSerializer, StationReviewSerializer


@extend_schema(
    summary="Список станций",
    description="Возвращает массив всех станций",
    tags=['Станции']
)
class StationListAPIView(generics.ListAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


@extend_schema(
    summary="Детальная информация о станции",
    description="Возвращает полную информацию о станции по id, включая отзывы",
    tags=['Станции']
)
class StationDetailAPIView(generics.RetrieveAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


@extend_schema(
    summary="Список отзывов",
    description="Возвращает массив всех отзывов на станции",
    tags=['Станции']
)
class StationReviewListAPIView(generics.ListAPIView):
    queryset = StationReview.objects.all()
    serializer_class = StationReviewSerializer

@extend_schema(
    summary="Создать станцию (Только для админов)",
    description="Создает новую станцию в каталоге",
    tags=['Станции']
)
class StationCreateAPIView(generics.CreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [IsAdminUser]