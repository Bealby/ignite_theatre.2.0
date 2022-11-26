from django.shortcuts import render
from .models import Show


def index(request):
    ''' A view to return index page'''

    shows = Show.objects.all()

    context = {
        'shows': shows,
    }

    return render(request, 'home/index.html', context)
