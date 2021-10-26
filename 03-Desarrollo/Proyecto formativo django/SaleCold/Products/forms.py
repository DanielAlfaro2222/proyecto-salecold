from django import forms
from django.forms import fields
from .models import Category

"""
¿Que significa ModelForm?

Un modelo es la representacion de una entidad de la base de datos en forma de clase, entonces un ModelForm es la representacion de los atributos de una clase en forma de elementos <input> de un formulario HTML, es decir que el ModelForm es el que se encarga de mapear los atributos de un modelo en forma de input de un formulario HTML.

Los campos de un ModelForm gestionan los datos y realizan la validacion de los datos cuando se envia un formulario.
"""

class FormularioCategoria(forms.ModelForm):
    """
    Clase para crear el formulario de la entidad categoria

    Es una instancia de la clase ModelForm

    Dentro de esta clase se crea una clase Meta en la cual se especifica que modelo vamos a afectar y que campos apareceran en el formulario
    """
    class Meta:
        """
        Clase que contiene los metadatos de el formulario

        * En la variable model se coloca el nombre del modelo al cual le vamos a crear un formulario.
        * En la variable fields se coloca que atributos de el modelo van a aparcer en el formulario, en este caso el valor __all__ significa que usaremos todos los atributos de el modelo.
        """
        model = Category
        fields = '__all__'