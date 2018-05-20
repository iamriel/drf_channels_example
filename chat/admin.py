from django.contrib import admin

from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
