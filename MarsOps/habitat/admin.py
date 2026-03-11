from django.contrib import admin
from .models import Habitat

@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'in_stock')
    list_filter = ('in_stock',)
    search_fields = ('name',)