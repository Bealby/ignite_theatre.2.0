# from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
# from tickets.models import Ticket


# def view_bag(request):
    # A view to return bag contents pages

#     return render(request, 'bag/bag.html')


# def add_to_bag(request, item_id):
#     '''Submit form to this view including ticket id and quanity'''
#     ''' Add a quantity of the specified tickets to the shopping bag'''

#     child_quantity = int(request.POST.get('child_quantity'))
#     adult_quantity = int(request.POST.get('adult_quantity'))
#     redirect_url = request.POST.get('redirect_url')
#     bag = request.session.get('bag', {})
#     '''Once in view get bag variable if exisits in session or create if doesnt'''

#     '''Add to bag'''

#     def add_quantity(quantity, item_id, bag):
#         if quantity:
#             if item_id in list(bag.keys()):
#                 bag[item_id] += quantity
#             else:
#                 bag[item_id] = quantity

#     if adult_quantity or child_quantity:

#         if adult_quantity:
#             add_quantity(
#                 adult_quantity,
#                 'adult_quantity',
#                 item_id,
#                 bag,)

#         if child_quantity:
#             add_quantity(
#                 child_quantity,
#                 'child_quantity',
#                 item_id,
#                 bag,)

#     request.session['bag'] = bag
#     return redirect(redirect_url)


# def adjust_bag(request, item_id):
#     """Adjust the quantity of the specified product to the specified amount"""

#     quantity = int(request.POST.get('quantity'))
#     bag = request.session.get('bag', {})

#     if quantity > 0:
#         bag[item_id] = quantity
#     else:
#         bag.pop(item_id)

#     request.session['bag'] = bag
#     return redirect(reverse('view_bag'))


# def remove_from_bag(request, item_id):
#     """Remove the item from the shopping bag"""

#     try:
#         bag = request.session.get('bag', {})
#         bag.pop(item_id)

#         request.session['bag'] = bag
#         return HttpResponse(status=200)

#     except Exception as e:
#         return HttpResponse(status=500)
