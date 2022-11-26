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
        'ticket_retail_address',
        'sponsor_image',
        'sponsor_name',
        'show_poster',
        'show_content',
    )


class UpcomingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
    )


admin.site.register(Show, ShowAdmin)
admin.site.register(Upcoming, UpcomingAdmin)
