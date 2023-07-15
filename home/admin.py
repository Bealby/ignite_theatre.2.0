from django.contrib import admin
from .models import Show
from .models import Upcoming


class ShowAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'ticket_retail_image',
        'ticket_retail_name',
        'ticket_retail_url',
        'ticket_retail_image_2',
        'ticket_retail_name_2',
        'ticket_retail_url_2',
        'ticket_retail_address',
        'show_poster',
        'show_sound_bite',
        'show_content',
    )


class UpcomingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'date',
        'location_2',
        'date_2',
        'location_3',
        'date_3',
        'position',
    )


admin.site.register(Show, ShowAdmin)
admin.site.register(Upcoming, UpcomingAdmin)
