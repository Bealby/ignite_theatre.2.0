from django.shortcuts import render
from .models import Show
from .models import Upcoming


def index(request):
    ''' A view to return index page'''

    shows = Show.objects.all()
    upcomings = Upcoming.objects.all()

    context = {
        'shows': shows,
        'upcomings': upcomings,
    }

    return render(request, 'home/index.html', context)
