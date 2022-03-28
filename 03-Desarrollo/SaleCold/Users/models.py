from django.db import models
from django.contrib.auth.models import User
from Orders.common import OrderStatus
from django.db.models import Q

class City(models.Model):
    id_city = models.AutoField("Id Ciudad", primary_key = True)
    description = models.CharField("Descripcion", null = True, blank = True, max_length=45)
    zip_code = models.CharField("Codigo postal", max_length = 6)
    create = models.DateTimeField('Fecha de creacion', auto_now_add = True)
    modified = models.DateTimeField('Fecha de modificacion', auto_now = True)
    state = models.BooleanField('Estado', default = True)

    def __str__(self):
        return self.description

    def length_zip_code(self):
        """Funcion complementaria para test unitarios"""
        return len(self.zip_code) <= 6

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        db_table = "city"
        ordering = ['id_city']

class TypeOfDocument(models.Model):
    id_type_of_document = models.AutoField("Id tipo de documento", primary_key=True)
    description = models.CharField("Descripcion", max_length=45)
    create = models.DateTimeField('Fecha de creacion', auto_now_add = True)
    modified = models.DateTimeField('Fecha de modificacion', auto_now=True)
    state = models.BooleanField('Estado', default = True)

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
    address = models.CharField("Direccion", max_length=70)
    neighborhood = models.CharField("Barrio/Localidad", max_length = 50)
    city = models.ForeignKey(City, verbose_name="Ciudad", on_delete=models.CASCADE)
    phone_number = models.CharField("Numero de telefono", max_length=15)
    gender = models.CharField("Genero", choices=GENDERS, default=FEMALE, max_length=6)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_orders_completed(self):
        return self.user.order_set.filter(state = OrderStatus.COMPLETED.value).order_by('-id_order')

    def get_orders_completed_and_canceled(self):
        return self.user.order_set.filter(Q(state = OrderStatus.COMPLETED.value) | Q(state = OrderStatus.CANCELED.value)).order_by('-id_order')

    def get_orders_payed(self):
        return self.user.order_set.filter(state = OrderStatus.PAYED.value).order_by('-id_order')

    class Meta:
        verbose_name = "Informacion adicional usuario"
        verbose_name_plural = "Informacion adicional usuarios"
        db_table = "user_model"
        ordering = ['id']