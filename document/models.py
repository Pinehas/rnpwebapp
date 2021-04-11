from django.db import models

# Create your models here.

class DocumentModel(models.Model):
    titre = models.CharField(max_length=200, null=False)
    categorie = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=False)
    acces = models.CharField(max_length=200, null=True)
    doc = models.FileField()
    date_ajout = models.DateField(auto_now_add=True, null=False)
    class Meta:
        db_table = "document"

