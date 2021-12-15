# Generated by Django 3.2.7 on 2021-12-11 02:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id_city', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Ciudad')),
                ('description', models.CharField(blank=True, max_length=45, null=True, verbose_name='Descripcion')),
                ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999)], verbose_name='Codigo postal')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'db_table': 'city',
                'ordering': ['id_city'],
            },
        ),
        migrations.CreateModel(
            name='TypeOfDocument',
            fields=[
                ('id_type_of_document', models.AutoField(primary_key=True, serialize=False, verbose_name='Id tipo de documento')),
                ('description', models.CharField(max_length=45, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de documento',
                'verbose_name_plural': 'Tipos de documento',
                'db_table': 'type_of_document',
                'ordering': ['id_type_of_document'],
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_document', models.CharField(max_length=20, verbose_name='Numero de documento')),
                ('address', models.CharField(max_length=70, verbose_name='Direccion')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Numero de telefono')),
                ('gender', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], default='Mujer', max_length=6, verbose_name='Genero')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.city', verbose_name='Ciudad')),
                ('type_of_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.typeofdocument', verbose_name='Tipo de documento')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Informacion adicional usuario',
                'verbose_name_plural': 'Informacion adicional usuarios',
                'db_table': 'user_model',
                'ordering': ['id'],
            },
        ),
    ]
