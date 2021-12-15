from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Products.models import Product
from Products.models import Category

def index(request):
    return render( request, 'index.html', context={
        'categorias': Category.objects.all(),
        'productos': Product.objects.exclude(discount= 0)[:5]
    } )

def info(request):
    return render(request, 'info.html', context={
        'categorias': Category.objects.all(),
    })

@login_required
def confirmPurchase(request):
    return render(request, 'confirmarCompra.html', context={})

@login_required
def manageDeliveries(request):
    return render(request, 'gestionarEntrega.html', context={})

@login_required
def addProduct(request):
    return render(request, 'agregarProducto.html', context={})