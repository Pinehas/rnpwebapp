from django.db import models

# Create your models here.

class MaterielModel(models.Model):
    nom = models.CharField(max_length=200, null=False)
    categorie = models.CharField(max_length=200, null=False)
    quantite = models.FloatField(null=False)
    prix = models.FloatField(null=False)
    marque = models.CharField(max_length=200, null=True)
    couleur = models.CharField(max_length=200, null=True)
    variete = models.CharField(max_length=200, null=True)
    guide = models.FileField()
    descr = models.CharField(max_length=200, null=False)
    date_ajout = models.DateField(auto_now_add=True ,null=False)
    class Meta:
        db_table = "materiel"

