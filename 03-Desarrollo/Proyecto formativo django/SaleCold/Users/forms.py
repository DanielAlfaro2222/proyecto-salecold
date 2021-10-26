from django import forms
from django.forms import fields
from .models import User

class FormularioRegistroUsuario(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 
                  'last_name', 
                  'username',
                  'password',
                  'email',
                  'type_of_document',
                  'number_document',
                  'address',
                  'city'
        ]