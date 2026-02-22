from django.shortcuts import render
from .models import MeechingHall


def index(request):
    ''' A view to return meeching hall page'''

    meeching_halls = MeechingHall.objects.all()

    context = {
        'meeching_halls': meeching_halls,
    }

    return render(request, 'meeching_hall/meeching_hall.html', context)