from django.contrib import admin
from .models import Category, Resources

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Resources)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('title', 'description')
