# Generated by Django 4.0.1 on 2022-03-23 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_city_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='neighborhood',
            field=models.CharField(default=' ', max_length=50, verbose_name='Barrio/Localidad'),
            preserve_default=False,
        ),
    ]
