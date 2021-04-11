from django.db import models

# Create your models here.

class PermissionModel(models.Model):
    id_personnel = models.IntegerField(null=False)
    service = models.CharField(max_length=200, null=False)
    poste = models.CharField(max_length=200, null=False)
    motif = models.CharField(max_length=200, null=False)
    piece_justif = models.FileField()
    duree = models.IntegerField(null=False)
    class Meta:
        db_table = "permission"

