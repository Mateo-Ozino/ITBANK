# Generated by Django 4.1 on 2022-08-18 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'managed': False, 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='direccion',
            options={'managed': False, 'verbose_name_plural': 'Direcciones'},
        ),
        migrations.AlterModelOptions(
            name='sucursal',
            options={'managed': False, 'verbose_name_plural': 'Sucursales'},
        ),
    ]