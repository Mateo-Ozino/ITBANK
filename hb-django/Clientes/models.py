from django.db import models

# Create your models here.
class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    calle = models.TextField()
    numero = models.IntegerField(blank=True, null=True)
    ciudad = models.TextField()
    provincia = models.TextField(blank=True, null=True)
    pais = models.TextField()

    class Meta:
        managed = False
        verbose_name_plural = "Direcciones"
        db_table = 'direccion'

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        verbose_name_plural = "Sucursales"
        db_table = 'sucursal'

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch = models.ForeignKey('Sucursal', models.DO_NOTHING)
    client_type = models.TextField(blank=True, null=True)
    direccion = models.ForeignKey('Direccion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        verbose_name_plural = "Clientes"
        db_table = 'cliente'
