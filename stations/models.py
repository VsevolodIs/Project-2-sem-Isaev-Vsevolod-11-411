from django.db import models
from django.contrib.auth.models import User


class Station(models.Model):
    name = models.CharField('Название станции', max_length=100)
    station_type = models.CharField('Тип станции', max_length=100)
    established_date = models.DateField('Дата создания', auto_now_add=True)
    crew_capacity = models.IntegerField('Вместимость экипажа', default=10)

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            total = sum(review.rating for review in reviews)
            return round(total / reviews.count(), 1)
        return None

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

    def __str__(self):
        return f"{self.name} ({self.station_type})"

class StationReview(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Автор")
    rating = models.IntegerField(default=5, verbose_name="Оценка")
    text = models.TextField('Отзыв')

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.station.name} - {self.author} - {self.rating}⭐"