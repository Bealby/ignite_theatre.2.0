from django.shortcuts import render
# from .models import Show
# from .models import Upcoming
from .models import MeechingHome


def index(request):
    ''' A view to return index page'''

    # shows = Show.objects.all()
    # upcomings = Upcoming.objects.all()
    meechings = MeechingHome.objects.all()

    context = {
        # 'shows': shows,
        # 'upcomings': upcomings,
        'meechings': meechings,
    }

    return render(request, 'home/index.html', context)
