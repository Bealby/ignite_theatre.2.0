from django.shortcuts import render
from .models import MeechingHall


def index(request):
    ''' A view to return meeching hall page'''

    meeching_hall = MeechingHall.objects.all()

    context = {
        'meeching_hall': meeching_hall,
    }

    return render(request, 'meeching_hall.html', context)