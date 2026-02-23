from django.contrib import admin
from .models import MeechingHall


class MeechingHallAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'ideas_url',
        'ideas_image',
        'memories_url',
        'memories_image',
        'petition_url',
        'petition_image',
        'meeching_hall_content',
        'meeching_hall_image',
    )

admin.site.register(MeechingHall, MeechingHallAdmin)
