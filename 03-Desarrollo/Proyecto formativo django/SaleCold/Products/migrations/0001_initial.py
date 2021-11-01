# Generated by Django 3.2.7 on 2021-11-01 21:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_category', models.AutoField(primary_key=True, serialize=False, verbose_name='Id categoria')),
                ('name', models.CharField(max_length=55, verbose_name='Nombre categoria')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'category',
                'ordering': ['id_category'],
            },
        ),
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id_unit_of_measure', models.AutoField(primary_key=True, serialize=False, verbose_name='Id unidad de medida')),
                ('name', models.CharField(max_length=45, verbose_name='Nombre unidad de medida')),
            ],
            options={
                'verbose_name': 'Unidad de medida',
                'verbose_name_plural': 'Unidades de medidas',
                'db_table': 'unit_of_measure',
                'ordering': ['id_unit_of_measure'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False, verbose_name='Id producto')),
                ('name', models.CharField(max_length=55, verbose_name='Nombre producto')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='products/images', verbose_name='Imagen del producto')),
                ('unit_price', models.PositiveIntegerField(verbose_name='Precio unitario')),
                ('stock', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Stock')),
                ('discount', models.PositiveSmallIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Descuento')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.category', verbose_name='Categoria')),
                ('unit_of_measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.unitofmeasure', verbose_name='Unidad de medida')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'product',
                'ordering': ['id_product'],
            },
        ),
    ]
