from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator 

class City(models.Model):
    id_city = models.AutoField("Id Ciudad", primary_key=True)
    description = models.CharField("Descripcion", null=True, blank=True, max_length=45)
    zip_code = models.PositiveIntegerField("Codigo postal", validators=[MinValueValidator(0), MaxValueValidator(999999)])

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        db_table = "city"
        ordering = ['id_city']

class TypeOfDocument(models.Model):
    id_type_of_document = models.AutoField("Id tipo de documento", primary_key=True)
    description = models.CharField("Descripcion", max_length=45)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documento"
        db_table = "type_of_document"
        ordering = ['id_type_of_document']

class User(AbstractUser):
    email = models.EmailField("Correo electronico", max_length=200)
    type_of_document = models.ForeignKey(TypeOfDocument, verbose_name="Tipo de documento", on_delete=models.CASCADE)
    number_document = models.CharField("Numero de documento", max_length=20, help_text="Numero de identificacion del usuario")
    address = models.CharField("Direccion", max_length=50, help_text="Direccion de residencia del usuario")
    city = models.ForeignKey(City, verbose_name="Ciudad", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "user"