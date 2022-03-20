from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import get_or_create_order
from Carts.utils import get_or_create_cart
from .utils import breadcrumb

@login_required
def order_view(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(request, cart)

    return render(request, 'orders/pedido.html', context = {
        'carrito': cart,
        'orden': order,
        'breadcrumb': breadcrumb(),
    })