from django.db import models

# Create your models here.


class VenteModel(models.Model):
    id_commande = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=False)
    class Meta:
        db_table = "vente"