from django.db import models

# Create your models here.

class PaiementManoeuvreModel(models.Model):
    id_projet = models.IntegerField(null=False)
    travail = models.CharField(max_length=200, null=False)
    nom = models.CharField(max_length=200, null=False)
    no_cni = models.CharField(max_length=200, null=True)
    duree = models.IntegerField(null=False)
    salaire = models.FloatField(null=False)
    date = models.DateTimeField(null=False)
    class Meta:
        db_table = "paiementmanoeuvre"

class AchatModel(models.Model):
    id_projet = models.IntegerField(null=False)
    designation = models.CharField(max_length=200, null=False)
    objet = models.CharField(max_length=200, null=False)
    prix = models.IntegerField(null=False)
    quantite = models.IntegerField(null=False)
    piece_facture = models.FileField(upload_to='media', null=True)
    date = models.DateTimeField(null=False)
    class Meta:
        db_table = "achat"

class PaiementSortantModel(models.Model):
    id_projet = models.IntegerField(null=False)
    sujet = models.CharField(max_length=200, null=False)
    objet = models.CharField(max_length=200, null=False)
    details = models.TextField(null=True)
    montant = models.FloatField(null=False)
    piece_recu = models.FileField(upload_to='media', null=True)
    date = models.DateTimeField(null=False)
    class Meta:
        db_table = "paiementsortant"

class PaiementEntrantModel(models.Model):
    id_projet = models.IntegerField(null=False)
    nature = models.CharField(max_length=200, null=False)
    details = models.TextField(null=False)
    montant = models.FloatField(null=False)
    montant_restant = models.FloatField(null=False)
    piece_entree = models.FileField(upload_to='media', null=True)
    date = models.DateTimeField(null=False)
    class Meta:
        db_table = "paiemententrant"

class CreditModel(models.Model):
    origine = models.CharField(max_length=200, null=False)
    objet = models.CharField(max_length=200, null=False)
    details = models.TextField(null=True)
    montant = models.FloatField(null=False)
    piece_credit = models.FileField(upload_to='media', null=True)
    date_remboursement = models.DateTimeField(null=False)
    date = models.DateField(null=False)
    class Meta:
        db_table = "credit"

class RemboursementModel(models.Model):
    id_credit = models.IntegerField(null=False)
    nature = models.CharField(max_length=200, null=True)
    details = models.TextField(null=False)
    montant = models.FloatField(null=False)
    piece_remboursement = models.FileField(upload_to='media', null=True)
    montant_restant = models.FloatField(null=False)
    date = models.DateTimeField(null=False)
    class Meta:
        db_table = "remboursement"


class CapitalModel(models.Model):
    origine = models.CharField(max_length=200, null=False)
    objet = models.CharField(max_length=200, null=False)
    details = models.CharField(max_length=200, null=True)
    montant = models.FloatField(null=False)
    piece_capital = models.FileField(upload_to='media', null=True)
    date = models.DateField(null=False)
    class Meta:
        db_table = "capital"
