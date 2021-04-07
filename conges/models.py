from django.db import models


# Create your models here.

class CongesModel(models.Model):
    id_personnel = models.IntegerField(null=False)
    debut = models.DateField(null=False)
    fin = models.DateField(null=False)
    class Meta:
        db_table = "conges"
