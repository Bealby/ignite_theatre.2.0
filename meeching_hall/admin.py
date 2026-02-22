from django.contrib import admin
from .models import MeechingHall


class MeechingHallAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'meeching_hall_petition',
        'meeching_hall_image',
        'meeching_hall_content',
    )

admin.site.register(MeechingHall, MeechingHallAdmin)
