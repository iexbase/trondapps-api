from django.contrib import admin

# Register your models here.
from app.models import Item, ItemStatus, ItemCategory


# Регистрация блока статусов
@admin.register(ItemStatus)
class ItemStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


# Регистрация категорий
@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'name', 'author', 'created_at', 'is_active']
    exclude = ('created_at', 'updated_at', 'slug')
    list_filter = ('created_at', 'is_active', 'category__name', 'status__name')
