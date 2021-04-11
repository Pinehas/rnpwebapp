from django.db import models

# Create your models here.

class ServiceModel(models.Model):
    nom = models.CharField(max_length=200, null=False)
    categorie = models.CharField(max_length=200, null=True)
    image_service = models.FileField()
    description = models.CharField(max_length=200, null=False)
    class Meta:
        db_table = "service"
