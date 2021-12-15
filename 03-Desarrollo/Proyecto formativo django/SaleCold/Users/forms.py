from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    name = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs = {
                    'autofocus': 'True',
                    'tab-index': 1,
                    'class': 'form-register__input',
                    'placeholder': 'Nombre'
        })
    )
    apellido = forms.CharField(
        required =True,
        widget = forms.TextInput(attrs = {
            'tab-index': 2,
            'class': 'form-register__input',
            'placeholder': 'Apellido'
        })
    )
    number_document = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs = {
            'tab-index': 3,
            'placeholder': 'Numero de documento',
            'class': 'form-register__input'
        })
    )
    address = forms.CharField(
        required=True,
        widget = forms.TextInput(attrs = {
            'tab-index': 4,
            'placeholder': 'Direccion de residencia',
            'class': 'form-register__input'
        })
    )
    phone_number = forms.CharField(
        required=True,
        widget = forms.TextInput(attrs = {
            'tab-index': 5,
            'placeholder': 'Numero telefonico',
            'class': 'form-register__input'
        })
    )
    email = forms.EmailField(
        required = True,
        widget = forms.EmailInput(attrs = {
            'tab-index': 6,
            'placeholder': 'Correo',
            'class': 'form-register__input'
        })
    )
    password = forms.CharField(
        required=True,
        widget = forms.PasswordInput(attrs = {
            'tab-index': 7,
            'placeholder': 'Contraseña',
            'class': 'form-register__input'
        })
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) > 30:
            raise forms.ValidationError('Este campo acepta maximo 30 caracteres')

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')

        if len(apellido) > 30:
            raise forms.ValidationError('Este campo acepta maximo 30 caracteres')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(username = email).exists():
            raise forms.ValidationError('El usuario ya esta registrado en el sistema')

        return email

    def clean_address(self):
        direccion = self.cleaned_data.get('address')

        if len(direccion) > 30:
            raise forms.ValidationError('Este campo acepta maximo 30 caracteres')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        mayusculas = 0
        numeros = 0
        simbolos = 0

        for caracter in password:
            if caracter in "!#$%&'()*+,-./:;=?{|}~[\]^_`@·½¬><":
                simbolos += 1
            elif caracter in '0123456789':
                numeros += 1
            elif caracter == caracter.upper():
                mayusculas += 1

        if mayusculas < 1 or numeros < 1 or simbolos < 1:
            raise forms.ValidationError('La contraseña debe tener minimo 8 caracteres y debe estar compuesta por 1 simbolo, 1 mayuscula y 1 numero')