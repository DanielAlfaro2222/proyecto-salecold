from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Products.models import Product
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET

@require_GET
def index(request):
    return render( request, 'index.html', context={
        'productos': Product.objects.filter(discount__gt = 0, stock__gt = 0).order_by('-discount')[:5]
    } )

@require_http_methods(['GET', 'POST'])
def info(request):
    return render(request, 'info.html', context={})

@require_http_methods(['GET', 'POST'])
def reset_password(request):
    contexto = {
        'usuario': User.objects.get(username = request.POST.get('correo'))
    }
