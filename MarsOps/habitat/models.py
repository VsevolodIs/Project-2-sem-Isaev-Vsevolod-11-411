from django.db import models
from stations.models import Station


class Habitat(models.Model):
    name = models.CharField('Название модуля', max_length=100)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, blank=True, related_name='habitats')
    capacity = models.IntegerField('Вместимость')
    in_stock = models.BooleanField('Активность', default=True)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __str__(self):
        station_name = self.station.name if self.station else "Не назначена"
        return f"{self.name} ({station_name})"