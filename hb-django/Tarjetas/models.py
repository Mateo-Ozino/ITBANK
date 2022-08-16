from django.db import models
from Clientes import models as Clientes_models

# Create your models here.
class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.IntegerField(unique=True)
    customer = models.ForeignKey(Clientes_models.Cliente, models.DO_NOTHING)
    cvv = models.IntegerField()
    creation_date = models.TextField()
    expire_date = models.TextField()
    card_type = models.TextField()
    brand = models.TextField()

    class Meta:
        managed = False
        db_table = 'tarjeta'