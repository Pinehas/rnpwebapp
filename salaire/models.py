from django.db import models

# Create your models here.

class SalaireModel(models.Model):
    id_personnel = models.IntegerField(null=False)
    montant = models.IntegerField(null=True)
    date = models.DateField(null=False)
    class Meta:
        db_table = "salaire"

