# Generated by Django 4.0.1 on 2022-03-05 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
        ('Carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(through='Carts.CartProducts', to='Products.Product'),
        ),
    ]
