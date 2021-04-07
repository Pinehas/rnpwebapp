from django.db import models

class Cmd_Prod_Model(models.Model):
    id_client = models.IntegerField(null=False)
    id_produit = models.IntegerField(null=False)
    quantite = models.IntegerField(null=False)
    details = models.CharField(max_length=2000, null=False)
    piece_cmd = models.FileField(upload_to='media', null=True)
    statut = models.CharField(max_length=200,null=True)
    date = models.DateField(auto_now_add=True, null=False)
    class Meta:
        db_table = "cmdproduit"

class Dmd_Serv_Model(models.Model):
    id_client = models.IntegerField(null=False)
    id_service = models.IntegerField(null=False)
    details = models.CharField(max_length=2000, null=False)
    piece_dmd = models.FileField(upload_to='media', null=True)
    statut = models.CharField(max_length=200,null=True)
    date = models.DateField(auto_now_add=True, null=False)
    class Meta:
        db_table = "dmdservice"