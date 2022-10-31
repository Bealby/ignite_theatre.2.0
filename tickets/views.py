from django.shortcuts import render, get_object_or_404
from .models import Show
from .models import Ticket


def all_tickets(request):
    '''context = to allow things to be sent to template'''
    
    tickets = Ticket.objects.all()
    '''Filter tickets by show'''
    shows = None

    '''Request if show exists'''
    if request.GET:
        if 'show' in request.GET:
            '''If show exists split into a list at the commas'''
            shows = request.GET['show'].split(',')
            '''Use the list to filter tickets only related to the show '''
            '''Name in Show.model '''
            tickets = tickets.filter(show__name__in=shows)
            '''Display to user which show they have currently selected'''
            shows = Show.objects.filter(name__in=shows)

    context = {
        'tickets': tickets,
        'current_shows': shows,
    }

    return render(request, 'tickets/tickets.html', context)


def ticket_detail(request, ticket_id):
    """ A view to show individual ticket details """

    ticket = get_object_or_404(Ticket, pk=ticket_id)

    context = {
        'ticket': ticket,
    }

    return render(request, 'tickets/ticket_detail.html', context)

