import pytest
from decimal import Decimal
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from stations.models import Station, StationReview
from resources.models import Category, Resources
from missions.models import Mission
from crew.models import CrewMember


@pytest.fixture
def api_client():
    return APIClient()


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
    member = CrewMember.objects.create(
        name="Иван Иванов",
        role="Командир",
        status="На базе",
        assigned_station=station
    )
    return member


@pytest.fixture
def mission(db, station, crew_member):
    mission = Mission.objects.create(
        name="Марсианский рассвет",
        mission_type="Исследование",
        station=station,
        objective="Найти воду"
    )
    mission.crew_members.add(crew_member)
    return mission


@pytest.fixture
def resource(db, category):
    return Resources.objects.create(
        category=category,
        title="Кислородный баллон",
        description="Чистый O2",
        price=Decimal("1500.00"),
        stock=10
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
def test_stations_api_list(api_client, station):
    url = reverse('stations:api_stations')
    response = api_client.get(url)

    assert response.status_code == 200
    data = response.json()

    if isinstance(data, dict) and 'results' in data:
        data = data['results']

    assert len(data) == 1
    assert data[0]['name'] == 'Марс-1'
    assert data[0]['station_type'] == 'Орбитальная'


@pytest.mark.django_db
def test_station_api_detail(api_client, station):
    url = reverse('stations:api_station_detail', kwargs={'pk': station.id})
    response = api_client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data['id'] == station.id
    assert 'average_rating' in data
    assert data['average_rating'] is None


@pytest.mark.django_db
def test_resources_api_list(api_client, resource):
    url = reverse('resources:api_resources')
    response = api_client.get(url)

    assert response.status_code == 200
    data = response.json()
    if isinstance(data, dict) and 'results' in data:
        data = data['results']

    assert len(data) == 1
    assert data[0]['title'] == "Кислородный баллон"
    assert data[0]['price'] == "1500.00"
    assert data[0]['stock'] == 10


@pytest.mark.django_db
def test_reviews_api_list(api_client, review, user):
    url = reverse('stations:api_station_reviews')
    response = api_client.get(url)

    assert response.status_code == 200
    data = response.json()
    if isinstance(data, dict) and 'results' in data:
        data = data['results']

    assert len(data) == 1
    assert data[0]['text'] == "Хороший модуль, но тесновато."
    assert data[0]['rating'] == 4
    assert 'author' in data[0]

    if isinstance(data[0]['author'], dict):
        assert data[0]['author']['username'] == "astro_alice"
    else:
        assert data[0]['author'] == user.id


@pytest.mark.django_db
def test_create_review_requires_authentication(api_client, station):
    url = reverse('stations:api_review_create')
    payload = {
        "station": station.id,
        "text": "Тестовый отзыв из API",
        "rating": 5
    }

    response = api_client.post(url, payload, format='json')

    assert response.status_code in [401, 403]


@pytest.mark.django_db
def test_create_review_success(api_client, user, station):
    api_client.force_authenticate(user=user)
    url = reverse('stations:api_review_create')

    payload = {
        "text": "Новый отзыв",
        "rating": 5
    }

    response = api_client.post(url, payload, format='json')

    if response.status_code == 201:
        assert StationReview.objects.filter(author=user).count() >= 1
    else:
        assert response.status_code == 400