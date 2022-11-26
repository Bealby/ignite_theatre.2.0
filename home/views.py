from django.shortcuts import render
from .models import NewShow
from .models import UpcomingShow


def index(request):
    ''' A view to return index page'''

    new_show = NewShow.objects.all()

    context = {
        'new_show': new_show,
    }

    return render(request, 'home/index.html', context)
