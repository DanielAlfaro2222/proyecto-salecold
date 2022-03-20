from .models import Order
from django.urls import reverse

def get_or_create_order(request, cart):
    order = cart.order

    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart = cart, user = request.user)

    if order:
        request.session['order_id'] = order.identifier

    return order

def breadcrumb(products = True, address = False, payment = False, confirm = False):
    return [
        {'title': 'Productos', 'active': products, 'url': reverse('Orders:order')},
        {'title': 'Dirección', 'active': address, 'url': reverse('Orders:order')},
        {'title': 'Pago', 'active': payment, 'url': reverse('Orders:order')},
        {'title': 'Confirmación', 'active': confirm, 'url': reverse('Orders:order')},
    ]