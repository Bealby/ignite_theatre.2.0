# from django.conf import settings
# from django.shortcuts import get_object_or_404
# from tickets.models import Ticket


# def bag_contents(request):

#     bag_items = []
#     '''Empty list for bag items to live in'''
#     total = 0
#     ticket_count = 0
#     bag = request.session.get('bag', {})

#     for item_id, adult_quantity in bag.items():
#         if adult_quantity.get('adult_quantity'):
#             ticket = get_object_or_404(Ticket, pk=item_id)
#             total += adult_quantity.get('adult_quantity') * ticket.adult_price
#             ticket_count += adult_quantity.get('adult_quantity')
#             bag_items.append({
#                 'item_id': item_id,
#                 'quantity': adult_quantity.get('adult_quantity'),
#                 'ticket': ticket,
#                 'adult_ticket': True,
#             })

#     for item_id, child_quantity in bag.items():
#         if child_quantity.get('child_quantity'):
#             ticket = get_object_or_404(Ticket, pk=item_id)
#             total += child_quantity.get('child_quantity') * ticket.child_price
#             ticket_count += child_quantity.get('child_quantity')
#             bag_items.append({
#                 'item_id': item_id,
#                 'quantity': child_quantity.get('child_quantity'),
#                 'ticket': ticket,
#                 'child_ticket': True,
#             })

#     grand_total = total

#     context = {
#         'bag_items': bag_items,
#         'total': total,
#         'ticket_count': ticket_count,
#         'grand_total': grand_total,
#     }

#     '''Make dictionary available to all templates across the enitire application'''
#     return context
