from django.db import models

# Create your models here.

class PersonnelModel(models.Model):
    nom = models.CharField(max_length=200, null=False)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=200, null=False)
    telephone = models.FloatField(null=False)
    password = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=False)
    email_pro = models.EmailField(null=False)
    pays = models.CharField(max_length=200, null=False)
    ville = models.CharField(max_length=200, null=False)
    quartier = models.CharField(max_length=200, null=False)
    date_recrutement = models.DateField()
    service = models.CharField(max_length=200, null=False)
    poste = models.CharField(max_length=200, null=False)
    acces = models.CharField(max_length=200, null=False)
    diplome_recrutement = models.CharField(max_length=200, null=False)
    type_contrat = models.CharField(max_length=200, null=False)
    cv = models.FileField()
    photo = models.FileField()
    num_cni = models.CharField(max_length=200, null=False)
    contrat = models.FileField()
    salaire = models.FloatField(null=False)
    class Meta:
        db_table = "personnel"
