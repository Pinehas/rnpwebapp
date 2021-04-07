from django.db import models


class ProduitModel(models.Model):
    nom = models.CharField(max_length=200, null=False)
    categorie = models.CharField(max_length=200, null=False)
    prix = models.FloatField(null=False)
    marque = models.CharField(max_length=200, null=True)
    couleur = models.CharField(max_length=200, null=True)
    variete = models.CharField(max_length=200, null=True)
    quantite = models.FloatField(null=False)
    descr = models.TextField(null=False)
    img_prod = models.FileField(upload_to='media', null=True)
    class Meta:
        db_table = "produit"



class EtatProdModel(models.Model):
    id_produit = models.IntegerField(null=False)
    nom = models.CharField(max_length=200, null=False)
    categorie = models.CharField(max_length=200, null=False)
    prix = models.FloatField(null=False)
    marque = models.CharField(max_length=200, null=True)
    couleur = models.CharField(max_length=200, null=True)
    variete = models.CharField(max_length=200, null=True)
    quantite = models.FloatField(null=False)
    descr = models.TextField(null=False)
    class Meta:
        db_table = "etatprod"

class BesoinProdModel(models.Model):
    nom = models.CharField(max_length=200, null=False)
    categorie = models.CharField(max_length=200, null=False)
    prix = models.FloatField(null=False)
    marque = models.CharField(max_length=200, null=True)
    couleur = models.CharField(max_length=200, null=True)
    variete = models.CharField(max_length=200, null=True)
    quantite = models.FloatField(null=False)
    descr = models.TextField(null=False)
    class Meta:
        db_table = "besoinprod"
