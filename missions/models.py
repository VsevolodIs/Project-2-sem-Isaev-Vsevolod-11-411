from django.db import models
from stations.models import Station
from crew.models import CrewMember


class Mission(models.Model):
    name = models.CharField('Название миссии', max_length=100)
    mission_type = models.CharField('Тип миссии', max_length=100)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='missions')
    crew_members = models.ManyToManyField(CrewMember, related_name='missions')
    status = models.CharField('Статус', max_length=100, default='planned')
    objective = models.TextField('Цель')

    class Meta:
        verbose_name = 'Миссия'
        verbose_name_plural = 'Миссии'

    def __str__(self):
        return f"{self.name} - {self.mission_type}"