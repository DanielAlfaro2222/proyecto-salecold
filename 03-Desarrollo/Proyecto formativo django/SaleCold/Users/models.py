from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator 
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
import uuid

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
    address = models.CharField("Direccion", max_length=70)
    city = models.ForeignKey(City, verbose_name="Ciudad", on_delete=models.CASCADE)
    phone_number = models.CharField("Numero de telefono", max_length=15)
    gender = models.CharField("Genero", choices=GENDERS, default=FEMALE, max_length=6)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = "Informacion adicional usuario"
        verbose_name_plural = "Informacion adicional usuarios"
        db_table = "user_model"
        ordering = ['id']

class Contact(models.Model):
    id_contact = models.AutoField('Id contacto', primary_key=True)
    ticket = models.CharField('Ticket', null=True, blank=True, max_length=7)
    subject = models.CharField('Asunto', max_length=50)
    first_name = models.CharField('Nombres', max_length=45)
    last_name = models.CharField('Apellidos', max_length=45)
    phone_number = models.CharField('Numero telefonico', max_length=20)
    email = models.EmailField('Correo', max_length=55)
    message = models.TextField('Mensaje')

    def __str__(self) -> str:
        return f'{self.ticket}'

    class Meta:
        verbose_name = "Contacto"
        db_table = "contact"
        ordering = ['id_contact']

def set_ticket_contact(sender, instance, *args, **kwargs):
    """
    Callback para asignar un numero de ticket unico a cada instancia de contacto.
    """

    if not instance.ticket:
        ticket = str(uuid.uuid4())[:7]

        while Contact.objects.filter(ticket = ticket).exists():
            ticket = str(uuid.uuid4())[:7]

        instance.ticket = ticket

# Conectar el callback con el modelo Contact
pre_save.connect(set_ticket_contact, sender=Contact)