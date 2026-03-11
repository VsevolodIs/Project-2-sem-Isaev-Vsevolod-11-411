from django.contrib import admin
from .models import Station

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'station_type', 'established_date',)
    list_filter = ('station_type',)
    search_fields = ('name',)