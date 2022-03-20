from django import forms
from django.contrib.auth.models import User
from Users.models import City
from Users.models import TypeOfDocument
from Users.models import UserModel
from django.contrib.auth import authenticate
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import reverse

CAMPO_OBLIGATORIO = 'Este campo es obligatorio.'
ERROR_CANTIDAD_CARACTERES = 'Este campo acepta minimo 4 caracteres y maximo 25 caracteres.'

class RegisterForm(forms.Form):
    GENDER = (
        (1, 'Genero'),
        (2, 'Hombre'),
        (3, 'Mujer'),
    )

    nombre = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
                    'autofocus': 'True',
                    'tab-index': 1,
                    'class': 'form-register__input',
                    'placeholder': 'Nombre'
        })
    )
    apellido = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'tab-index': 2,
            'class': 'form-register__input',
            'placeholder': 'Apellido'
        })
    )
    numero_documento = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'tab-index': 3,
            'placeholder': 'Numero de documento',
            'class': 'form-register__input'
        })
    )
    direccion = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'tab-index': 4,
            'placeholder': 'Direccion de residencia',
            'class': 'form-register__input'
        })
    )
    telefono = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'tab-index': 5,
            'placeholder': 'Numero telefonico',
            'class': 'form-register__input',
            'type': 'tel'
        })
    )
    email = forms.EmailField(
        required = False,
        widget = forms.TextInput(attrs = {
            'tab-index': 6,
            'placeholder': 'Correo',
            'class': 'form-register__input'
        })
    )
    contrasena = forms.CharField(
        required = False,
        widget = forms.PasswordInput(attrs = {
            'tab-index': 7,
            'placeholder': 'Contraseña',
            'class': 'form-register__input'
        })
    )
    ciudad = forms.ModelChoiceField(
        required = False,
        widget = forms.Select(attrs = {
            'class': 'container-select-register',
        }),
        queryset = City.objects.all(),
        empty_label = "Ciudad",
    )

    tipo_documento = forms.ModelChoiceField(
        required = False,
        widget = forms.Select(attrs = {
            'class': 'container-select-register',
        }),
        queryset = TypeOfDocument.objects.all(),
        empty_label = 'Tipo de documento',
    )

    genero = forms.TypedChoiceField(
        required = False,
        widget = forms.Select(attrs = {
            'class': 'container-select-register',
            'placeholder': 'Genero',
        }),
        empty_value = '1',
        choices = GENDER,
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')

        if len(nombre) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif len(nombre) < 4 or len(nombre) > 25:
            raise forms.ValidationError(ERROR_CANTIDAD_CARACTERES)

        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')

        if len(apellido) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif len(apellido) < 4 or len(apellido) > 25:
            raise forms.ValidationError(ERROR_CANTIDAD_CARACTERES)

        return apellido

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(username = email).exists():
            raise forms.ValidationError('El usuario ya esta registrado en el sistema.')
        elif len(email) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)

        return email

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')

        if len(direccion) > 30:
            raise forms.ValidationError('Este campo acepta maximo 30 caracteres.')
        elif len(direccion) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)

        return direccion

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento')

        if len(numero_documento) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        
        return numero_documento

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        if len(telefono) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif len(telefono) < 9 or len(telefono) > 15:
            raise forms.ValidationError('Este campo acepta minimo 4 caracteres y maximo 15 caracteres.')

        return telefono

    def clean_contrasena(self):
        contrasena = self.cleaned_data.get('contrasena')
        mayusculas = 0
        numeros = 0
        simbolos = 0

        for caracter in contrasena:
            if caracter in "!#$%&'()*+,-./:;=?{|}~[\]^_`@·½¬><":
                simbolos += 1
            elif caracter in '0123456789':
                numeros += 1
            elif caracter == caracter.upper():
                mayusculas += 1

        if len(contrasena) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif mayusculas < 1 or numeros < 1 or simbolos < 1:
            raise forms.ValidationError('La contraseña debe tener minimo 8 caracteres y debe estar compuesta por 1 simbolo, 1 mayuscula y 1 numero.')

        return contrasena
    
    def clean_ciudad(self):
        ciudad = self.cleaned_data.get('ciudad')

        if ciudad == None:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)

        return ciudad

    def clean_tipo_documento(self):
        tipo_documento = self.cleaned_data.get('tipo_documento')

        if tipo_documento == None:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        
        return tipo_documento

    def clean_genero(self):
        genero = self.cleaned_data.get('genero')

        if genero == '1':
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        
        return genero

    def save(self):
        user = User.objects.create_user(
            username = self.cleaned_data.get('email').strip(),
            email = self.cleaned_data.get('email').strip(),
            password = self.cleaned_data.get('contrasena'),
        )

        user.first_name = self.cleaned_data.get('nombre').strip()
        user.last_name = self.cleaned_data.get('apellido').strip()

        user.save()

        tipo_documento = TypeOfDocument.objects.get(
            description = self.cleaned_data.get('tipo_documento')
        )

        ciudad = City.objects.get(description = self.cleaned_data.get('ciudad'))

        UserModel.objects.create(
            user = user,
            type_of_document = tipo_documento,
            number_document = self.cleaned_data.get('numero_documento').strip(),
            address = self.cleaned_data.get('direccion').strip(),
            phone_number = self.cleaned_data.get('telefono').strip(),
            city = ciudad,
            gender = self.cleaned_data.get('genero').strip()
        )

        return user

    def send(self, request):
        template = get_template('mails/plantillaBienvenida.html')
        context = {
            'usuario': f"{self.cleaned_data.get('nombre').strip().split()[0]} {self.cleaned_data.get('apellido').strip().split()[0]}",
            'dominio': get_current_site(request).domain,
            'url': reverse('index'),
            'productos': Product.objects.filter(state = True, discount__gt = 0, stock__gt = 0).order_by('-discount')[:4],
        }
        content = template.render(context)

        email = EmailMultiAlternatives(
            subject = 'Bienvenid@ a SaleCold',
            body = '',
            from_email = settings.EMAIL_HOST_USER,
            to = [self.cleaned_data.get('email').strip()]
        )

        email.attach_alternative(content, 'text/html')

        email.send(fail_silently = False)

class ContactForm(forms.Form):
    nombre = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'tab-index': 1,
            'class': 'form-contact__input',
            'placeholder': 'Nombre',
            'autofocus': 'True'
        }),
        
    )
    apellido = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'tab-index': 2,
            'class': 'form-contact__input',
            'placeholder': 'Apellido',
        })
    )
    telefono = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'tab-index': 3,
            'class': 'form-contact__input',
            'placeholder': 'Telefono',
            'type': 'tel'
        })
    )
    correo = forms.EmailField(
        required = False,
        widget = forms.TextInput(attrs = {
            'tab-index': 4,
            'class': 'form-contact__input',
            'placeholder': 'Correo electronico',
        })
    )
    asunto = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'tab-index': 5,
            'class': 'form-contact__input',
            'placeholder': 'Asunto',
        })
    )
    mensaje = forms.CharField(
        required = False,
        widget = forms.Textarea(attrs = {
            'tab-index': 6,
            'class': 'form-contact__textarea',
            'placeholder': 'Mensaje',
        })
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')

        if len(nombre) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif len(nombre) < 4 or len(nombre) > 25:
            raise forms.ValidationError(ERROR_CANTIDAD_CARACTERES)

        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')

        if len(apellido) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif len(apellido) < 4 or len(apellido) > 25:
            raise forms.ValidationError(ERROR_CANTIDAD_CARACTERES)

        return apellido

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        if len(telefono) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif len(telefono) < 9 or len(telefono) > 15:
            raise forms.ValidationError('Este campo acepta minimo 9 caracteres y maximo 15 caracteres.')

        return telefono

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')

        if len(correo) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)

        return correo

    def clean_asunto(self):
        asunto = self.cleaned_data.get('asunto')

        if len(asunto) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif len(asunto) < 5 or len(asunto) > 30:
            raise forms.ValidationError('Este campo acepta minimo 5 caracteres y maximo 30 caracteres.')

        return asunto

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')

        if len(mensaje) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)

        return mensaje

    def send(self, request):
        template = get_template('mails/plantillaContacto.html')
        context = {
            'nombre': f"{self.cleaned_data.get('nombre').strip()} {self.cleaned_data.get('apellido').strip()}",
            'asunto': self.cleaned_data.get('asunto').strip(),
            'correo': self.cleaned_data.get('correo').strip(),
            'telefono': self.cleaned_data.get('telefono').strip(),
            'mensaje': self.cleaned_data.get('mensaje').strip(),
            'dominio': get_current_site(request).domain,
            'url': reverse('index')
        }
        content = template.render(context)

        email = EmailMultiAlternatives(
            subject = 'Nuevo mensaje de contacto',
            body = '',
            from_email = settings.EMAIL_HOST_USER,
            to = [settings.EMAIL_HOST_USER],
            cc = ['kdalfaro45@misena.edu.co']
        )

        email.attach_alternative(content, 'text/html')

        email.send(fail_silently = False)
        

class UpdateDataUserForm(forms.Form):
    nombre = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'class': 'container-label-form__input',
            'autofocus': 'True',
            'tab-index': 1
        })
    )

    apellido = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'class': 'container-label-form__input',
            'tab-index': 2,
        })
    )

    tipo_documento = forms.ModelChoiceField(
        required = False,
        widget = forms.Select(attrs = {
            'class': 'container-select-update-user',
            'tab-index': 3,
        }),
        queryset = TypeOfDocument.objects.all(),
    )

    numero_documento = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'class': 'container-label-form__input',
            'tab-index': 4,
        })
    )

    ciudad = forms.ModelChoiceField(
        required = False,
        widget = forms.Select(attrs = {
            'class': 'container-select-update-user',
            'tab-index': 5,
        }),
        queryset = City.objects.all(),
    )

    direccion = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'class': 'container-label-form__input',
            'tab-index': 6,
        })
    )

    correo = forms.EmailField(
        required = False,
        widget = forms.TextInput(attrs = {
            'class': 'container-label-form__input',
            'tab-index': 7,
        })
    )

    telefono = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs = {
            'class': 'container-label-form__input',
            'tab-index': 8,
            'type': 'tel'
        })
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')

        if len(nombre) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif len(nombre) < 4 or len(nombre) > 25:
            raise forms.ValidationError(ERROR_CANTIDAD_CARACTERES)

        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')

        if len(apellido) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif len(apellido) < 4 or len(apellido) > 25:
            raise forms.ValidationError(ERROR_CANTIDAD_CARACTERES)

        return apellido

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')

        if len(correo) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)

        return correo

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')

        if len(direccion) > 30:
            raise forms.ValidationError('Este campo acepta maximo 30 caracteres.')
        elif len(direccion) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)

        return direccion

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento')

        if len(numero_documento) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        
        return numero_documento

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        if len(telefono) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif len(telefono) < 9 or len(telefono) > 15:
            raise forms.ValidationError('Este campo acepta minimo 9 caracteres y maximo 15 caracteres.')

        return telefono
    
    def clean_ciudad(self):
        ciudad = self.cleaned_data.get('ciudad')

        if ciudad == None:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)

        return ciudad

    def clean_tipo_documento(self):
        tipo_documento = self.cleaned_data.get('tipo_documento')

        if tipo_documento == None:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        
        return tipo_documento

    def save(self, user):
        informacion_adicional = UserModel.objects.get(user = user)

        user.first_name = self.cleaned_data.get('nombre').strip()
        user.last_name = self.cleaned_data.get('apellido').strip()
        user.email = self.cleaned_data.get('correo').strip()
        user.username = self.cleaned_data.get('correo').strip()
        user.save()

        informacion_adicional.city = City.objects.get(
            description = self.cleaned_data.get('ciudad')
        )
        informacion_adicional.type_of_document = TypeOfDocument.objects.get(
            description = self.cleaned_data.get('tipo_documento')
        )
        informacion_adicional.number_document = self.cleaned_data.get('numero_documento').strip()
        informacion_adicional.address = self.cleaned_data.get('direccion').strip()
        informacion_adicional.phone_number = self.cleaned_data.get('telefono').strip()

        informacion_adicional.save()

class LoginForm(forms.Form):
    correo = forms.EmailField(
        required = False,
        widget = forms.TextInput(attrs = {
            'class': 'form-login__input',
            'autofocus': 'true',
            'tab-index': 1,
            'placeholder': 'Correo'
        })

    )
    contrasena = forms.CharField(
        required = False,
        widget = forms.PasswordInput(attrs = {
            'class': 'form-login__input',
            'tab-index': 2,
            'placeholder': 'Contraseña'
        })
    )

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')

        if len(correo) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)

        return correo

    def clean_contrasena(self):
        contrasena = self.cleaned_data.get('contrasena')

        if len(contrasena) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)

        return contrasena

    def authenticate_user(self):
        correo = self.cleaned_data.get('correo').strip()
        contrasena = self.cleaned_data.get('contrasena')

        return authenticate(username = correo, password = contrasena)

class ChangePassword(forms.Form):
    contrasena = forms.CharField(
        required = False,
        widget = forms.PasswordInput(attrs = {
            'autofocus': 'true',
            'tab-index': 1,
            'class': 'container-label-form-contraseña__input',
        })
    )

    contrasena2 = forms.CharField(
        required = False,
        widget = forms.PasswordInput(attrs = {
            'tab-index': 2,
            'class': 'container-label-form-contraseña__input',
        })
    )

    def clean_contrasena(self):
        contrasena = self.cleaned_data.get('contrasena')
        mayusculas = 0
        numeros = 0
        simbolos = 0

        for caracter in contrasena:
            if caracter in "!#$%&'()*+,-./:;=?{|}~[\]^_`@·½¬><":
                simbolos += 1
            elif caracter in '0123456789':
                numeros += 1
            elif caracter == caracter.upper():
                mayusculas += 1

        if len(contrasena) == 0:
            raise forms.ValidationError(CAMPO_OBLIGATORIO)
        elif mayusculas < 1 or numeros < 1 or simbolos < 1:
            raise forms.ValidationError('La contraseña debe tener minimo 8 caracteres y debe estar compuesta por 1 simbolo, 1 mayuscula y 1 numero.')

        return contrasena

    def clean(self):
        cleaned_data = super().clean()

        if len(cleaned_data.get('contrasena2')) == 0:
            self.add_error('contrasena2', CAMPO_OBLIGATORIO)
        elif cleaned_data.get('contrasena2') != cleaned_data.get('contrasena'):
            self.add_error('contrasena2', 'Las contraseñas deben coincidir.')