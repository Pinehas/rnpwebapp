from django.db import models
# Create your models here.

class ProjetModel(models.Model):
    designation = models.CharField(max_length=200, null=False)
    client = models.CharField(max_length=200, null=False)
    categorie = models.CharField(max_length=200, null=False)
    pays = models.CharField(max_length=200, null=False)
    ville = models.CharField(max_length=200, null=False)
    quartier = models.CharField(max_length=200, null=False)
    duree = models.IntegerField(null=False)
    contrat_projet = models.FileField(upload_to='media', null=True)
    tdr_projet = models.FileField(upload_to='media', null=True)
    cahier_projet = models.FileField(upload_to='media', null=True)
    date_contrat = models.DateField(null=False)
    date_debut = models.DateField(null=False)
    montant = models.FloatField(null=False)
    details = models.TextField(null=False)
    statut = models.CharField(max_length=200, null=True)
    date_lancement = models.DateField(null=True)
    date_fin = models.DateField(null=True)