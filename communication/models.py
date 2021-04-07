from django.db import models

# Create your models here.

class CommentaireModel(models.Model):
    nom = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=False)
    message = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=False)
    class Meta:
        db_table = "commentaire"



class ContactModel(models.Model):
    nom = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=False)
    objet = models.CharField(max_length=200, null=False)
    message = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=False)
    class Meta:
        db_table = "contact"
