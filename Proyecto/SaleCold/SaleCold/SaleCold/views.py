#Importamos la funcion render de la libreria django.shortcuts
from django.shortcuts import render

#Creamos la funcion que renderiza cada html de la pagina
def index(request):
    return render( request, 'index.html', context={} )

def login(request):
    return render( request, 'login.html', context={} )

def administrator(request):
    return render(request, 'administrador.html', context={} )

def info(request):
    return render(request, 'info.html', context={})

def contact(request):
    return render(request, 'contacto.html', context={})

def register(request):
    return render(request, 'register.html', context={})

def recuperation(request):
    return render(request, 'recuperacion.html', context={})

def recuperationPhone(request):
    return render(request, 'recuperacionViaCelular.html', context={})

def recuperationEmail(request):
    return render(request, 'recuperacionViaCorreo.html', context={})

def changePassword(request):
    return render(request, 'cambiarContrasena.html', context={})

def confirmPurchase(request):
    return render(request, 'confirmarCompra.html', context={})

def manageDeliveries(request):
    return render(request, 'gestionarEntrega.html', context={})

def userNormal(request):
    return render(request, 'usuarioNormal.html', context={})

def addProduct(request):
    return render(request, 'agregarProducto.html', context={})

def updateDataUser(request):
    return render(request, 'actualizarDatos.html', context={})