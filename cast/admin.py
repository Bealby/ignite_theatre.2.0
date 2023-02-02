from django.contrib import admin
from .models import Show
from .models import Actor
from .models import Crew
from .models import Cast


class ShowAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'gallery_show_link',
        'poster',
        'testimonial_2',
        'testimonial_3',
        'testimonial_3',
    )


class ActorAdmin(admin.ModelAdmin):
    list_display = (
        'show',
        'name',
        'image',
        'description',
        'website',
        'facebook',
        'position',
    )

    ordering = ('position',)


class CrewAdmin(admin.ModelAdmin):
    list_display = (
        'show',
        'name',
        'role',
        'position',
    )


class CastAdmin(admin.ModelAdmin):
    list_display = (
        'show',
        'name',
        'role',
        'position',
    )


admin.site.register(Show, ShowAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(Cast, CastAdmin)
