# Generated by Django 4.0.3 on 2022-03-27 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0015_remove_address_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='send_bill',
            field=models.BooleanField(default=False, verbose_name='Factura enviada'),
        ),
    ]
