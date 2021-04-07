from django.db import models

# Create your models here.

class DisciplineModel(models.Model):
    nom = models.CharField(max_length=200, null=False)
    objet = models.CharField(max_length=200, null=False)
    details = models.CharField(max_length=200, null=True)
    piece_disc = models.FileField(upload_to='media', null=True)
    date = models.DateTimeField(auto_now_add=True, null=False)
    class Meta:
        db_table = "discipline"

class ExplicationModel(models.Model):
    id_discipline = models.IntegerField(null=False)
    nom = models.CharField(max_length=200, null=False)
    objet = models.CharField(max_length=200, null=False)
    piece_expl = models.FileField(upload_to='media', null=True)
    date = models.DateTimeField(auto_now_add=True, null=False)
    class Meta:
        db_table = "explication"
