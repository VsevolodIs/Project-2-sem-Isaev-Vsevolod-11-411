from django.contrib import admin
from .models import Mission

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'mission_type', 'station', 'status')
    list_filter = ('mission_type', 'status')
    search_fields = ('name', 'description')
    filter_horizontal = ('crew_members',)
