from django.db import models

# Create your models here.
class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.IntegerField(unique=True)
    customer_id = models.IntegerField()
    cvv = models.IntegerField()
    creation_date = models.TextField()
    expire_date = models.TextField()
    card_type = models.TextField()
    brand = models.TextField()

    class Meta:
        managed = False
        db_table = 'tarjeta'