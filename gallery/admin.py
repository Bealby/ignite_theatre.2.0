from django.contrib import admin
from .models import Show
from .models import Gallery


class ShowAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'show',
        'name',
        'description',
        'image',
    )


admin.site.register(Show, ShowAdmin)
admin.site.register(Gallery, GalleryAdmin)
