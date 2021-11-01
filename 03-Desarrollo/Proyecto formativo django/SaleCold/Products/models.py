from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator 

class Category(models.Model):
    id_category = models.AutoField("Id categoria", primary_key = True)
    name = models.CharField("Nombre categoria", max_length = 55)
    description = models.CharField("Descripcion", null = True, blank = True, max_length = 255)

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
    description = models.CharField("Descripcion", null = True, blank = True, max_length = 255)
    image = models.ImageField("Imagen del producto", upload_to = "products/images")
    unit_price = models.PositiveIntegerField("Precio unitario")
    stock = models.PositiveSmallIntegerField("Stock", null = True, blank = True, default = 0)
    discount = models.PositiveSmallIntegerField("Descuento", null = True, blank = True, default = 0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    category = models.ForeignKey(Category, verbose_name = "Categoria", on_delete = models.CASCADE)
    unit_of_measure = models.ForeignKey(UnitOfMeasure, verbose_name = "Unidad de medida", on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "product"
        ordering = ['id_product']