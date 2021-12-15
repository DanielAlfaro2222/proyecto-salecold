from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import login 
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from Users.models import TypeOfDocument
from Users.models import UserModel
from Users.models import City
from django.contrib.auth.models import User
from django.contrib import messages
from Users.forms import RegisterForm
from django.db.utils import IntegrityError
from Products.models import Category
from Users.models import Contact

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':

        username = request.POST.get('correo')
        password = request.POST.get('contrasena')

        user = authenticate(username=username, password=password) 

        if user:
            login(request, user)
            if user.is_staff:
                return redirect('administrator')
            else:
                return redirect('index')
        else:
            messages.error(request, "Correo o contraseña incorrectos")
            
    return render(request, 'login.html', context = {
        'categorias': Category.objects.all(),
    })

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')

def register(request):

    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        correo = request.POST.get('email')
        contrasena = request.POST.get('password')
        user = User.objects.create_user(username=correo, email=correo, password=contrasena)
        user.first_name = request.POST.get('name')
        user.last_name = request.POST.get('apellido')
        user.save()

        tipo_documento = TypeOfDocument()
        tipo_documento.id_type_of_document = request.POST.get('tipo_documento')
        ciudad = City()
        ciudad.id_city = request.POST.get('ciudad')
        genero = request.POST.get('genero')

        informacion_adicional = UserModel.objects.create(
            user = user,
            type_of_document = tipo_documento,
            number_document = request.POST.get('number_document'),
            address = request.POST.get('address'),
            phone_number = request.POST.get('phone_number'),
            city = ciudad,
            gender = genero
        )

        login(request, user)
        return redirect('index')

    return render(request, 'users/register.html', context={
        'formulario': form,
        'TipoDeDocumento': TypeOfDocument.objects.all(),
        'City': City.objects.all(),
        'categorias': Category.objects.all(),
    })

def recuperation(request):
    return render(request, 'users/recuperacion.html', context={
        'categorias': Category.objects.all(),
    })

def recuperationPhone(request):
    return render(request, 'users/recuperacionViaCelular.html', context={
        'categorias': Category.objects.all(),
    })

def recuperationEmail(request):
    return render(request, 'users/recuperacionViaCorreo.html', context={
        'categorias': Category.objects.all(),
    })

@login_required
def changePassword(request):
    return render(request, 'users/cambiarContrasena.html', context={
        'categorias': Category.objects.all(),
    })

@login_required
def updateDataUser(request):
    tipos_de_documento = TypeOfDocument.objects.all()
    ciudades = City.objects.all()

    # Datos adicionales del usuario almacenados en el UserModel
    informacion_adicional = UserModel.objects.get(user = request.user)

    if request.method == 'POST':

        nombres = request.POST.get('nombre')
        apellidos = request.POST.get('apellido')
        tipo_documento = TypeOfDocument()
        tipo_documento.id_type_of_document = request.POST.get('tipo de documento')
        numero_documento = request.POST.get('numero de documento')
        ciudad = City()
        ciudad.id_city = request.POST.get('ciudad')
        direccion = request.POST.get('direccion')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')

        usuario = User.objects.get(username = request.user.email)
        usuario.first_name = nombres
        usuario.last_name = apellidos
        usuario.email = correo

        try:
            usuario.username = correo
            usuario.save()

            informacion_adicional.city = ciudad
            informacion_adicional.type_of_document = tipo_documento
            informacion_adicional.number_document = numero_documento
            informacion_adicional.address = direccion
            informacion_adicional.phone_number = telefono

            informacion_adicional.save()

            messages.success(request, "Informacion actualizada exitosamente")

        except IntegrityError:
            messages.error(request, 'El correo electronico ya esta registrado')

    return render(request, 'users/actualizarDatosUsuario.html', context={
            'informacion_adicional': informacion_adicional,
            'tipos_de_documento': tipos_de_documento,
            'ciudades': ciudades,
            'categorias': Category.objects.all(),
    })

@login_required
def panelUser(request):
    return render(request, 'users/panelConfiguracionUsuario.html', context={})

@login_required
def administrator(request):
    return render(request, 'users/administrador.html', context={} )

def contact(request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        Contact.objects.create(
            first_name = nombre,
            last_name = apellido,
            phone_number = telefono,
            email = correo,
            subject = asunto,
            message = mensaje
        )

        messages.success(request, 'Enviado con exito, en 24h un asesor se contactara contigo')

    return render(request, 'users/contacto.html', context={
        'categorias': Category.objects.all(),
    })