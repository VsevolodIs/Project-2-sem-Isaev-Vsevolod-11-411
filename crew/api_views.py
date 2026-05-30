from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema
from crew.models import CrewMember, CrewSkill, Profile
from crew.serializers import CrewMemberSerializer, ProfileSerializer


@extend_schema(
    summary="Список экипажа",
    description="Возвращает массив всех членов экипажа",
    tags=['Экипаж']
)
class CrewMemberListAPIView(generics.ListAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer


@extend_schema(
    summary="Профиль текущего пользователя",
    description=(
        "Возвращает профиль авторизованного пользователя: "
        "звание, опыт, биография, Telegram и аватар. Требует аутентификации"
    ),
    tags=['Экипаж']
)
class MyProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
