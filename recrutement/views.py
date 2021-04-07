from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recrutement/main.html')



def insert_offre(request):
    if request.method=="POST":
        if request.POST.get('poste') and request.POST.get('specialite') and request.POST.get('niveau') and request.POST.get('experience')\
                and request.POST.get('pays') and request.POST.get('ville') and request.POST.get('type_contrat')\
                and request.POST.get('details') and request.POST.get('date_pubplication')\
                and request.POST.get('date_limite'):
            saverecord=OffreModel()
            saverecord.poste=request.POST.get('poste')
            saverecord.specialite = request.POST.get('specialite')
            saverecord.niveau = request.POST.get('niveau')
            saverecord.experience = request.POST.get('experience')
            saverecord.pays = request.POST.get('pays')
            saverecord.ville = request.POST.get('ville')
            saverecord.type_contrat = request.POST.get('type_contrat')
            saverecord.details = request.POST.get('details')
            saverecord.date_pubplication = request.POST.get('date_pubplication')
            saverecord.date_limite = request.POST.get('date_limite')
            saverecord.save()
            messages.success(request, 'L''offre a été enregistré avec succès !')
            return render(request, 'recrutement/form_offre.html')
    else:
        return render(request, 'recrutement/form_offre.html')


def insert_demission(request):
    if request.method=="POST":
        if request.POST.get('id_personnel') and request.POST.get('motif') and request.POST.get('date'):
            saverecord=DemissionModel()
            saverecord.nom=request.POST.get('id_personnel')
            saverecord.couleur = request.POST.get('motif')
            saverecord.categorie = request.POST.get('date')
            saverecord.save()
            messages.success(request, 'La démission a été enregistré avec succès !')
            return render(request, 'recrutement/form_demission.html')
    else:
        return render(request, 'recrutement/form_demission.html')


def insert_licenciement(request):
    if request.method=="POST":
        if request.POST.get('id_personnel') and request.POST.get('motif') and request.POST.get('date'):
            saverecord = LicenciementModel()
            saverecord.nom = request.POST.get('id_personnel')
            saverecord.couleur = request.POST.get('motif')
            saverecord.categorie = request.POST.get('date')
            saverecord.save()
            messages.success(request, 'Le licenciement a été enregistré avec succès !')
            return render(request, 'recrutement/form_licenciement.html')
    else:
        return render(request, 'recrutement/form_licenciement.html')




