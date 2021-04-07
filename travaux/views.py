from django.shortcuts import render
from .models import *
from django.contrib import messages
from .forms import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    showdata=ProjetModel.objects.all()
    return render(request, 'travaux/main.html', {"data":showdata})


def insert_projet(request):
    if request.method=="POST":
        if request.POST.get('designation') and request.POST.get('client') and request.POST.get('categorie') and request.POST.get('pays')\
                and request.POST.get('ville') and request.POST.get('quartier') and request.POST.get('duree') and request.POST.get('date_contrat')\
                and request.POST.get('date_debut') and request.POST.get('montant') and request.POST.get('details') and request.POST.get('statut')\
                and request.POST.get('date_lancement') and request.POST.get('date_fin'):
            saverecord=ProjetModel()
            saverecord.designation=request.POST.get('designation')
            saverecord.client = request.POST.get('client')
            saverecord.categorie = request.POST.get('categorie')
            saverecord.pays = request.POST.get('pays')
            saverecord.ville = request.POST.get('ville')
            saverecord.quartier = request.POST.get('quartier')
            saverecord.duree = request.POST.get('duree')
            saverecord.date_contrat = request.POST.get('date_contrat')
            saverecord.date_debut = request.POST.get('date_debut')
            saverecord.montant = request.POST.get('montant')
            saverecord.details = request.POST.get('details')
            saverecord.statut = request.POST.get('statut')
            saverecord.date_lancement = request.POST.get('date_lancement')
            saverecord.date_fin = request.POST.get('date_fin')
            saverecord.save()
            messages.success(request, 'Le Projet a été enregistré avec succès !')
            return render(request, 'travaux/formulaire.html')
    else:
        return render(request, 'travaux/formulaire.html')

def editprojet(request,id):
    obj=ProjetModel.objects.get(id=id)
    return render(request,'travaux/edit_projet.html', {"data":obj})

def lancement(request,id):
    modprojet=ProjetModel.objects.get(id=id)
    form=projetforms(request.POST, instance=modprojet)
    if form.is_valid():
        form.save()
        messages.success(request, 'Le Produit modifié avec succès !')
    modprojet = ProjetModel.objects.get(id=id)
    return render(request,'travaux/edit_projet.html', {"data":modprojet})

def delProjet(request,id):
    deleteprojet=ProjetModel.objects.get(id=id)
    deleteprojet.delete()
    showdata=ProjetModel.objects.all()
    messages.success(request, 'Le Projet a été supprimé !')
    return render(request, 'travaux/main.html', {"data":showdata})


