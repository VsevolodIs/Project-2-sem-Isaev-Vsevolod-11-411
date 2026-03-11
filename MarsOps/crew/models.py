from django.db import models
from django.contrib.auth.models import User
from stations.models import Station


class CrewMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='crew_profile')
    name = models.CharField('Имя', max_length=100)
    role = models.CharField('Роль', max_length=100)
    status = models.CharField('Статус', max_length=100)
    assigned_station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Член экипажа'
        verbose_name_plural = 'Члены экипажа'

    def __str__(self):
        return f"{self.name} - {self.role} ({self.status})"

class CrewSkill(models.Model):
    crew_member = models.ForeignKey(CrewMember, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField('Навык', max_length=100)
    level = models.PositiveIntegerField('Уровень', default=1)

    class Meta:
        unique_together = ('crew_member', 'skill_name')
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return f"{self.crew_member} - {self.skill_name} ({self.level})"