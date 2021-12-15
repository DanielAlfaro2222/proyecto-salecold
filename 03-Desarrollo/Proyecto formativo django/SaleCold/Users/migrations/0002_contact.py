# Generated by Django 3.2.7 on 2021-12-15 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id_Contact', models.AutoField(primary_key=True, serialize=False, verbose_name='Id contacto')),
                ('ticket', models.CharField(blank=True, max_length=7, null=True, verbose_name='Ticket')),
                ('subject', models.CharField(max_length=50, verbose_name='Asunto')),
                ('first_name', models.CharField(max_length=45, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=45, verbose_name='Apellidos')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Numero telefonico')),
                ('email', models.EmailField(max_length=55, verbose_name='Correo')),
                ('message', models.TextField(verbose_name='Mensaje')),
            ],
        ),
    ]
