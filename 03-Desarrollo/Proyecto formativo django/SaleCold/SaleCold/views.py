#Importamos la funcion render de la libreria django.shortcuts
from django.shortcuts import render
from django.contrib.auth import login # Libreria para importar la funcion login
from django.contrib.auth import authenticate # Libreria para importar la funcion authenticate
from django.shortcuts import redirect # Libreria para importar la funcion redirect
from django.contrib import messages # Libreria para importar la funcion para mandar mensajes
from django.contrib.auth import logout # Libreria para importar la funcion logout
from django.contrib.auth.decorators import login_required # Libreria para importa la funcion login_required
from Users.models import TypeOfDocument
from Users.models import UserModel
from Users.models import City
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

def index(request):
    return render( request, 'index.html', context={} )

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) 

        if user != None:

            login(request, user)
            return redirect('index')
        else: 

            return render(request, 'login.html', context={'error': "Usuario o contraseña incorrectos"})
    return render(request, 'login.html', context= {})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def administrator(request):
    return render(request, 'administrador.html', context={} )

def info(request):
    return render(request, 'info.html', context={})

def contact(request):
    return render(request, 'contacto.html', context={})

def register(request):
    tiposDeDocumento = TypeOfDocument.objects.all()
    city = City.objects.all()
    mensaje = ""

    if request.POST:

        try:
            user_required = User.objects.create_user(username = request.POST.get('correo'),
                                            password = request.POST.get('contrasena'),
                                            email = request.POST.get('correo')
            )
            user_required.first_name = request.POST.get('nombre')
            user_required.last_name = request.POST.get('apellido')
            user_required.save()

            tipo_documento = TypeOfDocument()
            tipo_documento.id_type_of_document = request.POST.get('tipo_documento')
            ciudad = City()
            ciudad.id_city = request.POST.get('ciudad')

            users = UserModel.objects.create(user = user_required, 
                                            type_of_document = tipo_documento,
                                            number_document = request.POST.get('numero_documento'),
                                            address = request.POST.get('direccion'),
                                            city = ciudad,
                                            phone_number = request.POST.get('number_phone'),
                                            gender = request.POST.get('genero')
            )

            users.save()

            mensaje = "Registro almacenado correctamente"
        except IntegrityError:
            mensaje = "Error el usuario ya existe en el sistema"


    return render(request, 'register.html', context={'TipoDeDocumento': tiposDeDocumento,
        'City': city,
        'mensaje': mensaje
    })

@login_required
def recuperation(request):
    return render(request, 'recuperacion.html', context={})

@login_required
def recuperationPhone(request):
    return render(request, 'recuperacionViaCelular.html', context={})

@login_required
def recuperationEmail(request):
    return render(request, 'recuperacionViaCorreo.html', context={})

@login_required
def changePassword(request):
    return render(request, 'cambiarContrasena.html', context={})

@login_required
def confirmPurchase(request):
    return render(request, 'confirmarCompra.html', context={})

@login_required
def manageDeliveries(request):
    return render(request, 'gestionarEntrega.html', context={})

@login_required
def userNormal(request):
    return render(request, 'usuarioNormal.html', context={})

@login_required
def addProduct(request):
    return render(request, 'agregarProducto.html', context={})

@login_required
def updateDataUser(request):
    return render(request, 'actualizarDatos.html', context={})