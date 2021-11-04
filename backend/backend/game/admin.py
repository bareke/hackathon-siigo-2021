from django.contrib import admin

from .models import Room, Player

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("code", )
    list_filter = ("id", )
    search_fields = ("id", )


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("active", )
    list_filter = ("id", "active")
    search_fields = ("id", )
