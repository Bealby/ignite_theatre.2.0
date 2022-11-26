from django.contrib import admin
from .models import NewShow
from .models import UpcomingShow


class NewShowAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'image_ticket',
        'web_ticket',
        'address_ticket',
        'image_sponsor',
        'image_show',
        'content_show',
    )


class UpcomingShowAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
    )


admin.site.register(NewShow, NewShowAdmin)
admin.site.register(UpcomingShow, UpcomingShowAdmin)
