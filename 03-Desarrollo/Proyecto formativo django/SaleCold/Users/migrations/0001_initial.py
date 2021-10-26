# Generated by Django 3.2.7 on 2021-10-26 00:47

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo electronico')),
                ('number_document', models.CharField(help_text='Numero de identificacion del usuario', max_length=20, verbose_name='Numero de documento')),
                ('address', models.CharField(help_text='Direccion de residencia del usuario', max_length=50, verbose_name='Direccion')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
