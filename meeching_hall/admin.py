from django.contrib import admin
from .models import MeechingHall


class MeechingHallAdmin(admin.ModelAdmin):
    list_display = (
    )

admin.site.register(MeechingHall, MeechingHallAdmin)
