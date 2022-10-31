from django.shortcuts import render
from .models import Gallery
from .models import Show


def all_galleries(request):
    '''A view to show all images'''
    '''context = to allow things to be sent to template'''
    
    galleries = Gallery.objects.all()
    '''Filter gallery by show'''
    shows = None

    '''Request if show exists'''
    if request.GET:
        if 'show' in request.GET:
            '''If show exists split into a list at the commas'''
            shows = request.GET['show'].split(',')
            '''Use the list to filter gallery only related to the show '''
            '''Name in Show.model '''
            galleries = galleries.filter(show__name__in=shows)
            '''Display to user which show they have currently selected'''
            shows = Show.objects.filter(name__in=shows)

    context = {
        'galleries': galleries,
        'current_shows': shows,
    }

    return render(request, 'gallery/gallery.html', context)