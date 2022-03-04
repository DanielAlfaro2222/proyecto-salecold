from django.db import models
from django.contrib.auth.models import User
from Products.models import Product
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed
import uuid

class Cart(models.Model):
    id_cart = models.AutoField('Id carrito', primary_key = True)
    user = models.ForeignKey(User, verbose_name = 'Usuario', null = True, blank = True, on_delete = models.CASCADE)
    product = models.ManyToManyField(Product, verbose_name = 'Productos')
    total = models.PositiveIntegerField('Total', default = 0)
    subtotal = models.PositiveIntegerField('Subtotal', default = 0)
    create = models.DateTimeField('Fecha de creacion', auto_now_add = True)
    modified = models.DateTimeField('Fecha de modificacion', auto_now = True) 
    identifier = models.CharField('Identificador unico' , unique = True, max_length = 100)

    COMISION = 0.1 # Comision del 10%

    def __str__(self):
        return self.identifier

    def update_subtotal(self):
        self.subtotal = sum([ producto.final_price for producto in self.product.all() ])
        self.save()

    def update_total(self):
        self.total = self.subtotal + (self.subtotal * Cart.COMISION)
        self.save()

    def update_totals(self):
        self.update_subtotal()
        self.update_total()

    class Meta:
        verbose_name = 'Carrito de compras'
        verbose_name_plural = 'Carritos de compras'
        db_table = 'cart'
        ordering = ['id_cart']

def set_identifier_cart(sender, instance, *args, **kwargs):
    """Funcion callback para agregar un identificador unico a cada instancia del carrito"""
    if not instance.identifier:
        identifier = str(uuid.uuid4())

        # Recorrer todos los carritos de compras para comprobar si ya existe el identificador unico
        while Cart.objects.filter(identifier = identifier).exists():
            identifier = str(uuid.uuid4())

        instance.identifier = identifier


pre_save.connect(set_identifier_cart, sender = Cart)

def update_total_cart(sender, instance, action, *args, **kwargs):
    """Funcion callback para actualizar el subtotal y total de la instancia del carrito de compras"""
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()

m2m_changed.connect(update_total_cart, sender = Cart.product.through)