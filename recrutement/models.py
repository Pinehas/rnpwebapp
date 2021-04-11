from django.db import models

# Create your models here.


class OffreModel(models.Model):
    poste = models.CharField(max_length=200, null=False)
    specialite = models.CharField(max_length=200, null=False)
    niveau = models.CharField(max_length=200, null=False)
    experience = models.CharField(max_length=200, null=False)
    pays = models.CharField(max_length=200, null=False)
    ville = models.CharField(max_length=200, null=False)
    type_contrat = models.CharField(max_length=200, null=False)
    details = models.CharField(max_length=200, null=True)
    date_pubplication = models.DateField(null=False)
    date_limite = models.DateField(null=False)
    piece_offre = models.FileField()
    class Meta:
        db_table = "offre"

class DemissionModel(models.Model):
    id_personnel = models.IntegerField(null=False)
    motif = models.CharField(max_length=200, null=False)
    lettre = models.FileField()
    date = models.DateField(null=False)
    class Meta:
        db_table = "demission"


class LicenciementModel(models.Model):
    id_personnel = models.IntegerField(null=False)
    motif = models.CharField(max_length=200, null=False)
    piece_licenciement = models.FileField()
    date = models.DateField(null=False)
    class Meta:
        db_table = "licenciement"

class CandidatModel(models.Model):
    nom = models.CharField(max_length=200, null=False)
    poste = models.CharField(max_length=200, null=False)
    specialite = models.CharField(max_length=200, null=True)
    niveau = models.CharField(max_length=200, null=False)
    experience = models.CharField(max_length=200, null=True)
    pays = models.CharField(max_length=200, null=False)
    ville = models.CharField(max_length=200, null=False)
    motivation = models.CharField(max_length=200, null=True)
    cv_candidat = models.FileField(upload_to='media', null=False)
    piece_jointe_cand = models.FileField()
    date = models.DateField(null=False)
    class Meta:
        db_table = "candidat"
