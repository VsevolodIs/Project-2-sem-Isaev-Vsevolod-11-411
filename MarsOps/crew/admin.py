from django.contrib import admin
from crew.models import CrewMember, CrewSkill


@admin.register(CrewMember)
class CrewMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'status', 'assigned_station')
    list_filter = ('role', 'status')
    search_fields = ('name',)

@admin.register(CrewSkill)
class CrewSkillAdmin(admin.ModelAdmin):
    list_display = ('crew_member', 'skill_name', 'level')
    list_filter = ('skill_name',)