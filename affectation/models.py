from django.db import models

# Create your models here.

class AffectationModel(models.Model):
    matricule = models.FloatField(null=False)
    code_projet = models.CharField(max_length=200, null=False) # promotion, ordinaire, retrogarde, interime
    date = models.DateField()
    details = models.CharField(max_length=200, null=True)
    class Meta:
        db_table = "affectation"