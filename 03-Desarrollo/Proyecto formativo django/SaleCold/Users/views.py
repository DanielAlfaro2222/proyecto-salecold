from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import login 
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from Users.models import UserModel
from django.contrib import messages
from Users.forms import RegisterForm
from Users.forms import ContactForm
from Users.forms import UpdateDataUserForm
from Users.forms import LoginForm
from django.contrib.auth.models import User
from django.conf import settings
import threading 
from .forms import ChangePassword
from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET

@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    formulario = LoginForm(request.POST or None)
    
    if request.method == 'POST' and formulario.is_valid():
        user = formulario.authenticate_user() 

        if user:
            login(request, user)
            if user.is_staff:
                return redirect('Users:administrator')
            else:
                return redirect('index')
        else:
            messages.error(request, "Correo o contraseña incorrectos")
            
    return render(request, 'users/login.html', context = {'formulario': formulario})

@require_http_methods(['GET', 'POST'])
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('Users:login')

@require_http_methods(['GET', 'POST'])
def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            thread = threading.Thread(target = form.send(request))

            thread.start()

            login(request, user)

            return redirect('index')

    return render(request, 'users/register.html', context={
        'formulario': form,
    })

@require_http_methods(['GET', 'POST'])
@login_required
def updateDataUser(request):
    # Datos adicionales del usuario almacenados en el UserModel
    informacion_adicional = UserModel.objects.get(user = request.user)

    # Enviar los datos del usuario al formulario.
    formulario = UpdateDataUserForm({
        'nombre': request.user.first_name,
        'apellido': request.user.last_name,
        'tipo_documento': informacion_adicional.type_of_document,
        'numero_documento': informacion_adicional.number_document,
        'ciudad': informacion_adicional.city,
        'direccion': informacion_adicional.address,
        'correo': request.user.username,
        'telefono': informacion_adicional.phone_number,
    })

    if request.method == 'POST':
        formulario = UpdateDataUserForm(request.POST or None)
        email = request.POST.get('correo')

        if User.objects.filter(email = email).exists() and email != request.user.username:
            messages.error(request, "Error el correo ya se encuentra registrado en el sistema")
        else:
            if formulario.is_valid():
                formulario.save(request.user)
                messages.success(request, "Informacion actualizada exitosamente")

    return render(request, 'users/actualizarDatosUsuario.html', context={
        'formulario': formulario,
    })

@require_GET
@login_required
def dashboardUser(request):
    return render(request, 'users/dashboardUsuario.html', context={})

@require_GET
@login_required
def administrator(request):
    return render(request, 'users/administrador.html', context={} )

@require_http_methods(['GET', 'POST'])
def contact(request):
    formulario = ContactForm(request.POST or None)

    if request.method == 'POST' and formulario.is_valid():
        formulario.send(request)
        messages.success(request, 'Enviado con exito, en 24h un asesor se contactara contigo')
        return redirect('Users:contact')

    return render(request, 'users/contacto.html', context={
        'formulario': formulario,
    })

@require_http_methods(['GET', 'POST'])
@login_required
def changePassword(request):
    formulario = ChangePassword(request.POST or None)

    if request.method == 'POST' and formulario.is_valid():
        usuario = User.objects.get(username = request.user.username)
        usuario.set_password = request.POST.get('contrasena')   
        usuario.save()

        messages.success(request, 'La contraseña se ha cambiado con exito.')

    return render(request, 'users/cambiarContrasena.html', context = {
        'formulario': formulario,
    })