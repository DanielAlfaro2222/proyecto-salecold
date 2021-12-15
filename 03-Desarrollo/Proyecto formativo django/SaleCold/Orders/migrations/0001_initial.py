# Generated by Django 3.2.7 on 2021-12-11 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderOrdered',
            fields=[
                ('id_header_ordered', models.AutoField(primary_key=True, serialize=False, verbose_name='Id cabecera pedido')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha pedido')),
                ('state', models.BooleanField(default=False, verbose_name='Pedido confirmado')),
                ('payment_reference', models.CharField(max_length=45, verbose_name='Referencia de pago')),
            ],
            options={
                'verbose_name': 'Cabecera pedido',
                'verbose_name_plural': 'Cabecera pedidos',
                'db_table': 'header_ordered',
                'ordering': ['id_header_ordered'],
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id_payment_type', models.AutoField(primary_key=True, serialize=False, verbose_name='Id tipo de pago')),
                ('description', models.CharField(max_length=45, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de pago',
                'verbose_name_plural': 'Tipos de pagos',
                'db_table': 'payment_type',
                'ordering': ['id_payment_type'],
            },
        ),
        migrations.CreateModel(
            name='TypeAccountingDocument',
            fields=[
                ('id_type_accounting_document', models.AutoField(primary_key=True, serialize=False, verbose_name='Id tipo documento contable')),
                ('nature', models.CharField(max_length=45, verbose_name='Naturaleza')),
            ],
            options={
                'verbose_name': 'Tipo documento contable',
                'verbose_name_plural': 'Tipos documentos contables',
                'db_table': 'type_accounting_document',
                'ordering': ['id_type_accounting_document'],
            },
        ),
        migrations.CreateModel(
            name='TypeOfDelivery',
            fields=[
                ('id_type_of_delivery', models.AutoField(primary_key=True, serialize=False, verbose_name='Id tipo de entrega')),
                ('description', models.CharField(max_length=45, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de entrega',
                'verbose_name_plural': 'Tipos de entregas',
                'db_table': 'type_of_delivery',
                'ordering': ['id_type_of_delivery'],
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id_order_detail', models.AutoField(primary_key=True, serialize=False, verbose_name='Id detalle pedido')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('subtotal', models.IntegerField(verbose_name='Subtotal')),
                ('total', models.IntegerField(verbose_name='Total')),
                ('header_ordered', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Orders.headerordered', verbose_name='Cabecera pedido')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Detalle pedido',
                'verbose_name_plural': 'Detalle pedidos',
                'db_table': 'order_detail',
                'ordering': ['id_order_detail'],
            },
        ),
        migrations.AddField(
            model_name='headerordered',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.paymenttype', verbose_name='Tipo de pago'),
        ),
        migrations.AddField(
            model_name='headerordered',
            name='type_accounting_document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.typeaccountingdocument', verbose_name='Tipo documento contable'),
        ),
        migrations.AddField(
            model_name='headerordered',
            name='type_of_delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.typeofdelivery', verbose_name='Tipo de entrega'),
        ),
        migrations.AddField(
            model_name='headerordered',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente'),
        ),
    ]
