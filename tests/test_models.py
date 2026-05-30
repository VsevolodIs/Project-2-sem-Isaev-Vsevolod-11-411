import pytest
from django.db import IntegrityError
from django.contrib.auth.models import User

from stations.models import Station, StationReview
from habitat.models import Habitat
from crew.models import CrewMember, CrewSkill
from resources.models import Category, Resources
from missions.models import Mission


@pytest.fixture
def user(db):
    return User.objects.create_user(username="astro_alice", password="mars123")


@pytest.fixture
def category(db):
    return Category.objects.create(name="Вода", slug="water")


@pytest.fixture
def station(db):
    return Station.objects.create(
        name="Марс-1",
        station_type="Орбитальная",
        crew_capacity=50
    )


@pytest.fixture
def crew_member(db, station):
    return CrewMember.objects.create(
        name="Иван Иванов",
        role="Командир",
        status="На базе",
        assigned_station=station
    )


@pytest.fixture
def review(db, user, station):
    return StationReview.objects.create(
        station=station,
        author=user,
        rating=4,
        text="Хороший модуль, но тесновато."
    )

@pytest.mark.django_db
class TestStation:
    def test_str(self, station):
        assert str(station) == "Марс-1 (Орбитальная)"

    def test_default_capacity(self, db):
        s = Station.objects.create(name="Фобос", station_type="Наземная")
        assert s.crew_capacity == 10

    def test_average_rating_no_reviews(self, station):
        assert station.average_rating is None

    def test_average_rating_with_reviews(self, station, user, review):
        StationReview.objects.create(
            station=station, author=user, text="Супер!", rating=5
        )
        station.refresh_from_db()
        assert station.average_rating == 4.5

@pytest.mark.django_db
class TestStationReview:
    def test_default_rating(self, db, user, station):
        r = StationReview.objects.create(station=station, author=user, text="Норм")
        assert r.rating == 5

@pytest.mark.django_db
class TestResources:
    def test_str(self, db, category):
        resource = Resources.objects.create(
            category=category,
            title="Кислородный баллон",
            price="1500.00"
        )
        assert str(resource) == "Кислородный баллон (1500.00)"

    def test_defaults(self, db, category):
        resource = Resources.objects.create(
            category=category,
            title="Вода",
            price="100.00"
        )
        assert resource.stock == 0
        assert resource.is_available is True

@pytest.mark.django_db
class TestMission:
    def test_str(self, station, crew_member):
        mission = Mission.objects.create(
            name="Марсианский рассвет",
            mission_type="Исследование",
            station=station,
            status="planned",
            objective="Найти воду"
        )
        assert str(mission) == "Марсианский рассвет - Исследование"

    def test_default_status(self, db, station):
        mission = Mission.objects.create(
            name="Тест", mission_type="Тест", station=station
        )
        assert mission.status == "planned"


@pytest.mark.django_db
class TestProfileSignals:
    def test_auto_created_on_user_create(self):
        new_user = User.objects.create_user(username="bob", password="pass")
        assert hasattr(new_user, 'profile')
        assert new_user.profile.telegram == ""
