from django.db import models

# Create your models here.

class ClientModel(models.Model):
    nom = models.CharField(max_length=200, null=False)
    categorie = models.CharField(max_length=200, null=False) # entreprise, , startup, particulier.
    telephone = models.FloatField(null=False)
    email = models.EmailField(null=False)
    pays = models.CharField(max_length=200, null=False)
    ville = models.CharField(max_length=200, null=False)
    quartier = models.CharField(max_length=200, null=False)
    profil = models.FileField(upload_to='media', null=False)
    password = models.CharField(max_length=200, null=False)
    date_inscription = models.DateField(auto_now_add=True, null=False)
    class Meta:
        db_table = "client"

class MessageClientModel(models.Model):
    id_client = models.IntegerField(null=False)
    message = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=False)
    piece_client = models.FileField(upload_to='media', null=True)

    class Meta:
        db_table = "messageclient"

class ReponseClientModel(models.Model):
    id_client = models.IntegerField(null=False)
    message = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=False)
    piece_service = models.FileField(upload_to='media', null=True)

    class Meta:
        db_table = "reponseclient"


