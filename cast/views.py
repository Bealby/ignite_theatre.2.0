from django.shortcuts import render
from .models import Show
from .models import Cast
from .models import Crew
from .models import Actor


def all_casts(request):
    '''context = to allow things to be sent to template'''
    
    casts = Cast.objects.all()
    crews = Crew.objects.all()
    actors = Actor.objects.all()
    '''Filter casts by show'''
    shows = None

    '''Request if show exists'''
    if request.GET:
        if 'show' in request.GET:
            '''If show exists split into a list at the commas'''
            shows = request.GET['show'].split(',')
            '''Use the list to filter gallery only related to the show '''
            '''Name in Show.model '''
            casts = casts.filter(show__name__in=shows)
            crews = crews.filter(show__name__in=shows)
            actors = actors.filter(show__name__in=shows)    
            '''Display to user which show they have currently selected'''
            shows = Show.objects.filter(name__in=shows)

    context = {
        'casts': casts,
        'crews': crews,
        'actors': actors,
        'current_shows': shows,
    }

    return render(request, 'cast/cast.html', context)