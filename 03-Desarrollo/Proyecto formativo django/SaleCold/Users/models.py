from django.db import models
from django.contrib.auth.models import User
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

class UserModel(models.Model):
    MALE = 'Hombre'
    FEMALE = 'Mujer'
    GENDERS = [(MALE, 'Hombre'), (FEMALE, 'Mujer')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    type_of_document = models.ForeignKey(TypeOfDocument, verbose_name="Tipo de documento", on_delete=models.CASCADE)
    number_document = models.CharField("Numero de documento", max_length=20)
    address = models.CharField("Direccion", max_length=50)
    city = models.ForeignKey(City, verbose_name="Ciudad", on_delete=models.CASCADE)
    phone_number = models.CharField("Numero de telefono", max_length=15)
    gender = models.CharField("Genero", choices=GENDERS, default=FEMALE, max_length=6)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "user_model"