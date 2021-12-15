from Products.models import Category
from Products.models import Product
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .utils import random_products
from django.db.models import Q

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/producto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        context['producto'] = context['object']
        context['productos_aleatorios'] = random_products(context['object'])
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/categoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        context['categoria'] = context['object']
        context['productos'] = context['categoria'].products.all()

        return context

class ProductSearchListView(ListView):
    template_name = 'products/busqueda producto.html'

    def query(self):
        # Funcion para retornar la consulta realizada por el usuario en el formulario de busqueda.
        return self.request.GET.get('q')

    def get_queryset(self):
        # Filtros para realizar la busqueda de los productos por el nombre y por el nombre de la categoria a la que pertenecen
        filters = Q(name__icontains = self.query()) | Q(description__icontains = self.query())

        return Product.objects.filter(filters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Categorias del menu
        context['categorias'] = Category.objects.all()
        # Consulta realizada por el usuario
        context['query'] = self.query()
        # Resultado de los productos que coinciden con la busqueda realizada por el usuario en el formulario.
        context['productos'] = self.get_queryset()
        context['cantidad_productos'] = self.get_queryset().count()
        return context 