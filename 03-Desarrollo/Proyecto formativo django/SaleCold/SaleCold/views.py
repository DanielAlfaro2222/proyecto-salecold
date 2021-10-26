from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render( request, 'index.html', context={} )

def login_view(request):
    """
    Funcion para realizar el login

    Acepta como parametro un objeto de tipo request
    """

    if request.method == 'POST': # Verificar que los datos se esten enviando por el metodo POST

        username = request.POST.get('username') # Tomar el valor ingresado por el usuario en el input con el name username
        password = request.POST.get('password') # Tomar el valor ingresado por el usuario en el input con el name password

        user = authenticate(username=username, password=password) # Llama a la funcion authenticate para verificar que el usuario este creado, si el usuario esta creado en el sistema la funcion retornara un objeto con toda la informacion del usuario y si el usuario no esta creado o no existe en el sistema la funcion retornara un None.
        
        if user != None: # Condicional para verificar que el valor que esta almacenado en la variable user sea distinto de none

            login(request, user) # Esta funcion recibe un objeto de tipo request y otro de tipo user, toma el id del usuario y lo guarda en la sesion.

            messages.success(request, f'Bienvenido {user.username}') # Enviar un mensaje para indicar que el inicio de sesion se realizo de manera correcta.

            return redirect('index') # Si el inicio de sesion fue correcto, la funcion redireccionara al usuario al index del aplicativo
        else: 
            messages.error(request, 'Usuario o contraseña incorrecta') # Mandar un mensaje de error en caso de que el inicio de sesion fuera incorrecto.

    return render(request, 'login.html', context= { # Renderiza el template del login
    })

def logout_view(request):

    logout(request) # Esta funcion recibe un objeto de tipo request y eliminar el id del usuario de la sesion
    messages.success(request, 'Sesión finalizada') # Mandar un mensaje de confirmacion
    return redirect('login') # Redireccionar al usuario al login

@login_required(login_url= '/login/')
def administrator(request):
    return render(request, 'administrador.html', context={} )

def info(request):
    return render(request, 'info.html', context={})

def contact(request):
    return render(request, 'contacto.html', context={})

def register(request):
    return render(request, 'register.html', context={})

@login_required(login_url= '/login/')
def recuperation(request):
    return render(request, 'recuperacion.html', context={})

@login_required(login_url= '/login/')
def recuperationPhone(request):
    return render(request, 'recuperacionViaCelular.html', context={})

@login_required(login_url= '/login/')
def recuperationEmail(request):
    return render(request, 'recuperacionViaCorreo.html', context={})

@login_required(login_url= '/login/')
def changePassword(request):
    return render(request, 'cambiarContrasena.html', context={})

@login_required(login_url= '/login/')
def confirmPurchase(request):
    return render(request, 'confirmarCompra.html', context={})

@login_required(login_url= '/login/')
def manageDeliveries(request):
    return render(request, 'gestionarEntrega.html', context={})

@login_required(login_url= '/login/')
def userNormal(request):
    return render(request, 'usuarioNormal.html', context={})

@login_required(login_url= '/login/')
def addProduct(request):
    return render(request, 'agregarProducto.html', context={})

@login_required(login_url= '/login/')
def updateDataUser(request):
    return render(request, 'actualizarDatos.html', context={})