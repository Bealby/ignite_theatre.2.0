from django.shortcuts import render
from .models import Show
from .models import Upcoming
from .models import Meeching


def index(request):
    ''' A view to return index page'''

    shows = Show.objects.all()
    upcomings = Upcoming.objects.all()
    meechings = Meeching.objects.all()

    context = {
        'shows': shows,
        'upcomings': upcomings,
        'meechings': meechings,
    }

    return render(request, 'home/index.html', context)
