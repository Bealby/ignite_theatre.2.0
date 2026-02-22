from django.shortcuts import render
from .models import MeechingHall


def index(request):
    ''' A view to return meeching hall page'''

    halls = MeechingHall.objects.all()

    context = {
        'halls': halls,
    }

    return render(request, 'meeching_hall/meeching_hall.html', context)