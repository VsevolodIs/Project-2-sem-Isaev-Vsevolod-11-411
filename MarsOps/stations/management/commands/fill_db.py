from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from crew.models import Profile, CrewMember, CrewSkill
from stations.models import Station, StationReview
from resources.models import Resources, Category
from missions.models import Mission
from habitat.models import Habitat
from random import choice, randint, sample
from django.utils import timezone


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = self._create_users()
        categories = self._create_categories()
        resources = self._create_resources(categories)
        stations = self._create_stations()
        habitats = self._create_habitats()
        crew_members = self._create_crew_members(users, stations)
        self._create_missions(stations, crew_members)
        self._create_reviews(users, stations)

        self.stdout.write(self.style.SUCCESS("БД заполнена"))

    def _create_users(self):
        User = get_user_model()
        users = []

        if not User.objects.filter(username="admin").exists():
            admin = User.objects.create_superuser("admin", "admin@mars.com", "admin123")
            Profile.objects.get_or_create(user=admin)
            self.stdout.write("Создали суперюзера")

        for i in range(1, 4):
            user, created = User.objects.get_or_create(username = f"user_{i}", defaults={"email": f"user_{i}@mail.com"})

            if created:
                user.set_password("qwerty123")
                user.save()
                Profile.objects.get_or_create(user=user)
                self.stdout.write(f"Это мы создали юзера {user.username}")
            users.append(user)
        return users

    def _create_categories(self):
        names = ["Еда", "Энергия", "Материалы"]
        categories = []

        for name in names:
            cat, _ = Category.objects.get_or_create(name=name, defaults={"slug": name.lower()})
            categories.append(cat)
        self.stdout.write("Создали категории")
        return categories

    def _create_resources(self, categories):
        titles = ["Ресурс 1", "Ресурс 2", "Ресурс 3"]
        resources = []

        for i in range(10):
            cat = choice(categories)
            prod, _ = Resources.objects.get_or_create(
                title=f"{choice(titles)} {i + 1}",
                defaults={
                    "category": cat,
                    "description": "Супер классный ресурс",
                    "price": randint(1000, 50000),
                    "stock": randint(5, 20),
                }
            )
            resources.append(prod)
        self.stdout.write("Создали ресурсы")
        return resources

    def _create_stations(self):
        stations_data = ["Марс-1", "Олимп", "Фобос"]
        stations = []

        for station_data in stations_data:
            station, created = Station.objects.get_or_create(
                name=station_data,
                defaults={
                    "station_type": station_data,
                    "crew_capacity": randint(5, 15),
                    "operational": choice([True, False]),
                }
            )
            stations.append(station)

        self.stdout.write("Создали станции")
        return stations

    def _create_habitats(self):
        habitats_data = ["Складской модуль", "Научный модуль", "Жилой модуль А"]
        habitats = []

        for habitat_data in habitats_data:
            habitat, created = Habitat.objects.get_or_create(
                name=habitat_data,
                defaults={
                    "capacity": randint(2, 10),
                    "in_stock": choice([True, False]),
                }
            )
            habitats.append(habitat)

        self.stdout.write("Создали модули")
        return habitats

    def _create_crew_members(self, users, stations):
        roles = ['commander', 'engineer', 'scientist', 'medic', 'pilot']
        statuses = ['active', 'mission']

        crew_members = []

        for user in users:
            station = choice(stations)
            crew, created = CrewMember.objects.get_or_create(
                user=user,
                defaults={
                    "name": f"{user.username}",
                    "role": choice(roles),
                    "status": choice(statuses),
                    "assigned_station": station
                }
            )
            crew_members.append(crew)

        self.stdout.write("Создали членов экипажа")
        return crew_members

    def _create_missions(self, stations, crew_members):
        mission_types = ['exploration', 'research', 'resource', 'maintenance']
        statuses = ['planned', 'active', 'completed', 'failed']

        mission_names = [
            "Исследование северного кратера", "Сбор образцов", "Ремонт  солнечных панелей",
            "Поиск воды", "Научные эксперименты"
        ]

        for i in range(8):
            station = choice(stations)
            mission, created = Mission.objects.get_or_create(
                name=f"{choice(mission_names)} #{i + 1}",
                station=station,
                defaults={
                    "mission_type": choice(mission_types),
                    "objective": "Выполнить важную миссию",
                    "status": choice(statuses),
                }
            )

            if created and crew_members:
                mission.crew_members.set(sample(crew_members, min(randint(2, 5), len(crew_members))))

        self.stdout.write("Создали миссии")

    def _create_reviews(self, users, stations):
        for i in range(5):
            StationReview.objects.get_or_create(
                author=choice(users),
                station=choice(stations),
                defaults={
                    "text": "Все супер!",
                    "rating": 5
                }
            )
        self.stdout.write("Создали отзывы")