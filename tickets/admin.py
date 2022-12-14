from django.contrib import admin
from .models import Show
from .models import Ticket


class ShowAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'poster',
    )


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'show',
        'name',
        'event_date',
        'place',
        'location',
        'image',
        'position',
        'description',
        'event_details',
        'price_details',
        'web',
        'date',
        'adult_price',
        'child_price',
    )

    ordering = ('position',)


admin.site.register(Show, ShowAdmin)
admin.site.register(Ticket, TicketAdmin)
