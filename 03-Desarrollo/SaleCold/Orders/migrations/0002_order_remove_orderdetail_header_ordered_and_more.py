# Generated by Django 4.0.1 on 2022-03-12 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False, verbose_name='Id orden')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha pedido')),
                ('state', models.CharField(choices=[(1, 'Creado'), (2, 'Pagado'), (3, 'Completado'), (4, 'Cancelado')], default='Creado', max_length=10, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
                'db_table': 'order',
                'ordering': ['id_order'],
            },
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='header_ordered',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='product',
        ),
        migrations.AddField(
            model_name='paymenttype',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymenttype',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion'),
        ),
        migrations.AddField(
            model_name='paymenttype',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='typeaccountingdocument',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='typeaccountingdocument',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion'),
        ),
        migrations.AddField(
            model_name='typeaccountingdocument',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='typeofdelivery',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='typeofdelivery',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion'),
        ),
        migrations.AddField(
            model_name='typeofdelivery',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.DeleteModel(
            name='HeaderOrdered',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.paymenttype', verbose_name='Tipo de pago'),
        ),
        migrations.AddField(
            model_name='order',
            name='type_accounting_document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.typeaccountingdocument', verbose_name='Tipo documento contable'),
        ),
        migrations.AddField(
            model_name='order',
            name='type_of_delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.typeofdelivery', verbose_name='Tipo de entrega'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente'),
        ),
    ]