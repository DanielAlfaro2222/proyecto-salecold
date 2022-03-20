from django.shortcuts import render
from .models import Cart
from .utils import get_or_create_cart
from Products.models import Product
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from .models import CartProducts
from django.contrib import messages
from django.http import HttpResponseRedirect

@require_GET
def cart_view(request):
    cart = get_or_create_cart(request)

    return render(request, 'cart/carrito de compras.html', context = {
        'carrito': cart,
    })

@require_POST
def add_product(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk = request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))

    cart_product = CartProducts.objects.create_or_update_quantity(cart, product, quantity)

    if quantity == 1:
        messages.success(request, 'Producto agregado al carrito exitosamente.')
    else:
        messages.success(request, 'Productos agregados al carrito exitosamente.')

    url_peticion = request.POST.get('url')

    return HttpResponseRedirect(url_peticion)

@require_POST
def remove_product(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk = request.POST.get('product_id'))

    cart.product.remove(product)
    messages.success(request, 'Producto eliminado del carrito.')

    return redirect('Carts:cart')

@require_GET
def clear_cart(request):
    # Se obtiene el carrito de compras
    cart = get_or_create_cart(request)

    # Mediante cartproducts_set se accede a los datos de la tabla intermedia que se creo en la relacion muchos a muchos entre Cart y Product, luego usando los metodos all() y delete() eliminamos todos los productos que estan relacionados con el carrito.
    cart.cartproducts_set.all().delete()
    cart.total = 0
    cart.subtotal = 0
    cart.save()

    messages.success(request, 'Carrito vaciado exitosamente.')
    return redirect('Carts:cart')

@require_POST
def modify_quantity(request):
    # Se obtiene el carrito de compras
    cart = get_or_create_cart(request)

    # Se captura la accion a realizar (agregar o disminuir cantidad)
    action = request.POST.get('action')

    # Se captura el producto que se le va a modificar la cantidad
    product = request.POST.get('product_id')
    cart = cart.cartproducts_set.get(product = product)

    if action == 'aumentar-cantidad':
        cart.quantity += 1
        cart.save()
    else:
        cart.quantity -= 1
        cart.save()

    return redirect('Carts:cart')
