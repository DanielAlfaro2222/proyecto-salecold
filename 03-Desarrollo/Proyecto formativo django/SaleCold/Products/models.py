from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator 
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid

class UnitOfMeasure(models.Model):
    id_unit_of_measure = models.AutoField("Id unidad de medida", primary_key = True)
    name = models.CharField("Nombre unidad de medida", max_length = 45)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Unidad de medida"
        verbose_name_plural = "Unidades de medidas"
        db_table = "unit_of_measure"
        ordering = ['id_unit_of_measure']

class Product(models.Model):
    id_product = models.AutoField("Id producto", primary_key = True)
    name = models.CharField("Nombre producto", max_length = 55)
    description = models.TextField("Descripcion", null = True, blank = True)
    image = models.ImageField("Imagen del producto", upload_to = "products/images")
    unit_price = models.PositiveIntegerField("Precio unitario")
    reference = models.CharField("Codigo", null=True, blank=True, max_length=10)
    stock = models.PositiveSmallIntegerField("Stock", null = True, blank = True, default = 0)
    discount = models.PositiveSmallIntegerField("Descuento", null = True, blank = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    unit_of_measure = models.ForeignKey(UnitOfMeasure, verbose_name = "Unidad de medida", on_delete = models.CASCADE)
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='Ruta')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "product"
        ordering = ['id_product']

def set_slug_product(sender, instance, *args, **kwargs):
    """
    Callback para asignar un codigo de referencia y un slug unico al producto antes de guardar el registro en la base de datos.

    Esta funcion recibe como parametro el modelo y la instancia.
    """
    # Verificar que la instancia no tenga un slug asignado
    if instance.name and not instance.slug:

        # Crea un slug con el nombre del producto
        slug = slugify(instance.name)
        reference = str(uuid.uuid4())[:10]

        # Crear una consulta a la base de datos para revisar si el slug ya existe, si existe entonces creamos un nuevo slug
        while Product.objects.filter(slug = slug).exists():
            slug = slugify(
                f'{instance.name}-{str(uuid.uuid4())[:8]}'
            )

        while Product.objects.filter(reference = reference).exists():
            reference = str(uuid.uuid4())[:10]

        instance.slug = slug
        instance.reference = reference

# Conectar el callback con el modelo
pre_save.connect(set_slug_product, sender=Product)

class Category(models.Model):
    id_category = models.AutoField("Id categoria", primary_key = True)
    name = models.CharField("Nombre categoria", max_length = 55)
    description = models.CharField("Descripcion", null = True, blank = True, max_length = 255)
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='Ruta')
    products = models.ManyToManyField(Product, verbose_name='Productos')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "category"
        ordering = ['id_category']

    @classmethod
    def create(cls, id_category, name, description):
        category = cls(id_category = id_category, name = name, description = description)
        return category

def set_slug_category(sender, instance, *args, **kwargs):
    """
    Callback para asignar un slug unico a la categoria antes de guardar la instancia.
    """
    if instance.name and not instance.slug:
        slug = slugify(instance.name)

        while Category.objects.filter(slug = slug).exists():
            slug = slugify(
                f'{instance.name}-{str(uuid.uuid4())[:8]}'
            )

        instance.slug = slug
    

# Conectar el callback con el modelo Category
pre_save.connect(set_slug_category, sender=Category)