from django.db import models


# Create your models here.

class MissionModel(models.Model):
    id_personnel = models.FloatField(null=False)
    objet = models.CharField(max_length=200, null=False)
    details = models.TextField(null=False)
    pays = models.CharField(max_length=200, null=True)
    ville = models.CharField(max_length=200, null=True)
    ordre = models.FileField(upload_to='media', null=True)
    debut = models.DateField(null=False)
    fin = models.DateField(null=False)
    class Meta:
        db_table = "mission"

class RapportMissionModel(models.Model):
    id_mission = models.FloatField(null=False)
    rapport = models.FileField(upload_to='media', null=True)
    date = models.DateTimeField(null=False)
    class Meta:
        db_table = "rapportmission"
