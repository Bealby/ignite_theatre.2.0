from django.conf import settings
from django.shortcuts import get_object_or_404
from tickets.models import Ticket


def bag_contents(request):

    bag_items = []
    '''Empty list for bag items to live in'''
    total = 0
    ticket_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        ticket = get_object_or_404(Ticket, pk=item_id)
        total += quantity * ticket.price
        ticket_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'ticket': ticket,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'ticket_count': ticket_count,
        'grand_total': grand_total,
    }
    
    '''Make dictionary available to all templates across the enitire application'''
    return context