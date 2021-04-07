from django.db import models

# Create your models here.

class ConferenceModel(models.Model):
    objet = models.CharField(max_length=200, null=False)
    frequence = models.CharField(max_length=200, null=False)
    date = models.DateField(null=True)
    heure = models.TimeField(null=False)
    class Meta:
        db_table = "conference"

class InvitationModel(models.Model):
    id_conference = models.IntegerField(null=False)
    id_personnel = models.IntegerField(null=False)
    class Meta:
        db_table = "invitation"

class PresenceModel(models.Model):
    id_conference = models.IntegerField(null=False)
    id_personnel = models.IntegerField(null=False)
    frequence = models.CharField(max_length=200, null=False)
    date = models.DateField(null=True)
    heure = models.TimeField(null=False)
    class Meta:
        db_table = "presence"

class Chat(models.Model):
    id_conference = models.IntegerField(null=False)
    id_personnel = models.IntegerField(null=False)
    id_cible = models.IntegerField(null=False)
    texte = models.CharField(max_length=5000, null=False)
    piece_chat = models.FileField(upload_to='media', null=True)
    heure = models.DateTimeField(auto_now_add=True, null=False)
    class Meta:
        db_table = "chat"

class NoteModel(models.Model):
    type_note = models.CharField(max_length=200,null=False)
    texte = models.CharField(max_length=5000,null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    piece_note = models.FileField(upload_to='media', null=True)

    class Meta:
        db_table = "note"

class AnnonceModel(models.Model):
    objet = models.CharField(max_length=200 ,null=False)
    texte = models.CharField(max_length=5000,null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    piece_annonce = models.FileField(upload_to='media', null=True)
    class Meta:
        db_table = "annonce"