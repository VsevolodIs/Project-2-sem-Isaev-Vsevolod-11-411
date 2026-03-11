from django.db import models

class Station(models.Model):
    name = models.CharField('Название станции', max_length=100)
    station_type = models.CharField('Тип станции', max_length=100)
    established_date = models.DateField('Дата создания', auto_now_add=True)
    crew_capacity = models.IntegerField('Вместимость экипажа', default=10)

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

    def __str__(self):
        return f"{self.name} ({self.station_type})"