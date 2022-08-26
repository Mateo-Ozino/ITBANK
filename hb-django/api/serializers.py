from dataclasses import fields
from rest_framework import serializers
from Clientes.models import Cliente, Sucursal, Direccion
from Cuentas.models import Cuenta
from django.contrib.auth.models import User
from Prestamos.models import Prestamo
from Tarjetas.models import Tarjeta

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        #indicamos que use todos los campos
        fields = ['customer_id', 'customer_name', 'customer_surname', 'customer_dni', 'dob', 'client_type', 'direccion']
        #les decimos cuales son los de solo lectura
        read_only_fields = (
            "customer_id",
        )

class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['account_id', 'customer_id', 'balance', 'iban', 'account_type']
        read_only_fields = (
            "account_id",
        )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['loan_id', 'loan_type', 'loan_date', 'loan_total', 'customer_id']

class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ['card_id', 'card_number','customer', 'cvv', 'creation_date', 'expire_date', 'card_type', 'brand']

class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['branch_id', 'branch_number', 'branch_name', 'branch_address_id', 'direccion']

class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = ['direccion_id', 'calle', 'numero', 'ciudad', 'provincia', 'pais']

    # direccion_id = models.AutoField(primary_key=True)
    # calle = models.TextField()
    # numero = models.IntegerField(blank=True, null=True)
    # ciudad = models.TextField()
    # provincia = models.TextField(blank=True, null=True)
    # pais = models.TextField()
