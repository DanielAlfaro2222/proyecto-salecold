from django.db import models
from Products.models import Product

class TypeOfDelivery(models.Model):
    id_type_of_delivery = models.AutoField('Id tipo de entrega', primary_key = True)
    description = models.CharField('Descripcion', max_length=45)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Tipo de entrega'
        verbose_name_plural = 'Tipos de entregas'
        db_table = 'type_of_delivery'
        ordering = ['id_type_of_delivery']

class TypeAccountingDocument(models.Model):
    id_type_accounting_document = models.AutoField('Id tipo documento contable', primary_key = True)
    nature = models.CharField('Naturaleza', max_length=45)

    def __str__(self):
        return self.nature

    class Meta:
        verbose_name = 'Tipo documento contable'
        verbose_name_plural = 'Tipos documentos contables'
        db_table = 'type_accounting_document'
        ordering = ['id_type_accounting_document']

class PaymentType (models.Model):
    id_payment_type = models.AutoField('Id tipo de pago', primary_key= True)
    description = models.CharField('Descripcion', max_length=45)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Tipo de pago'
        verbose_name_plural = 'Tipos de pagos'
        db_table = 'payment_type'
        ordering = ['id_payment_type']


class HeaderOrdered(models.Model):
    id_header_ordered = models.AutoField('Id cabecera pedido', primary_key = True)
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha pedido')
    state = models.BooleanField('Disponible', default=True)
    payment_reference = models.CharField('Referencia de pago', max_length=45)
    type_of_delivery = models.ForeignKey(TypeOfDelivery, verbose_name='Tipo de entrega', on_delete = models.CASCADE)
    type_accounting_document = models.ForeignKey(TypeAccountingDocument, verbose_name='Tipo documento contable', on_delete = models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, verbose_name='Tipo de pago', on_delete = models.CASCADE)

    def __str__(self):
        return self.order_date

    class Meta:
        verbose_name = 'Cabecera pedido'
        verbose_name_plural = 'Cabecera pedidos'
        db_table = 'header_ordered'
        ordering = ['id_header_ordered']

class OrderDetail(models.Model):
    id_order_detail = models.AutoField('Id detalle pedido', primary_key=True)
    quantity = models.IntegerField('Cantidad')
    subtotal = models.IntegerField('Subtotal')
    total = models.IntegerField('Total')
    product = models.ForeignKey(Product, verbose_name='Producto', on_delete = models.CASCADE )
    header_ordered = models.OneToOneField(HeaderOrdered, verbose_name='Cabecera pedido', on_delete = models.CASCADE )

    def __str__(self):
        return self.total

    class Meta: 
        verbose_name = 'Detalle pedido'
        verbose_name_plural = 'Detalle pedidos'
        db_table = 'order_detail'
        ordering = ['id_order_detail']