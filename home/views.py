from django.shortcuts import render
# from .models import Show
# from .models import Upcoming
from .models import MeechingHall


def index(request):
    ''' A view to return index page'''

    # shows = Show.objects.all()
    # upcomings = Upcoming.objects.all()
    halls = MeechingHall.objects.all()

    context = {
        # 'shows': shows,
        # 'upcomings': upcomings,
        'halls': halls,
    }

    return render(request, 'home/index.html', context)
