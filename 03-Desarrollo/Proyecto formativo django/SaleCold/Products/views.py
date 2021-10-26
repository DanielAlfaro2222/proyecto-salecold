from django.shortcuts import render
from django.http import HttpRequest
from .forms import FormularioCategoria

class FormularioCategoriaView(HttpRequest):
    """
    Esta clase se usa para recibir la informacion del formulario y posteriormente si la informacion es valida se almacenara en la base de datos mediante la funcion metodoProcesarFormulario()
    """

    def index(request):
        categoria = FormularioCategoria()
        return render(request, "registroCategoria.html", {"form": categoria})

    def metodoProcesarFormulario(request):
        """
        Esta funcion recibe un objeto de tipo request con todos los datos de la peticion y procesa la informacion que el usuario ingreso en los campos del formulario, luego revisa que los datos esten correctos y por ultimo los almacena en la base de datos
        """
        categoria = FormularioCategoria(request.POST)

        if categoria.is_valid():
            categoria.save()
            categoria = FormularioCategoria()

        return render(request, "registroCategoria.html", {"form": categoria, "mensaje": "Registro almacenado correctamente"})