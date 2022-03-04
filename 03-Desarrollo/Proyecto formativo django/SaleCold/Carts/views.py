from django.shortcuts import render
from .models import Cart
from .utils import get_or_create_cart
from Products.models import Product
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def cart_view(request):
    cart = get_or_create_cart(request)

    return render(request, 'cart/carrito de compras.html', context = {
        'carrito': cart,
    })

@require_http_methods(['GET', 'POST'])
def add_product(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk = request.POST.get('product_id'))

    cart.product.add(product)

    return redirect('Carts:cart')

@require_http_methods(['GET', 'POST'])
def remove_product(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk = request.POST.get('product_id'))

    cart.product.remove(product)

    return redirect('Carts:cart')