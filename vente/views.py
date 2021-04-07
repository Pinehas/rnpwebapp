from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'vente/main.html')

def insert_vente(request):
    if request.method=="POST":
        if request.POST.get('id_commande') and request.POST.get('date'):
            saverecord=VenteModel()
            saverecord.nom=request.POST.get('id_commande')
            saverecord.couleur = request.POST.get('date')
            saverecord.save()
            messages.success(request, 'Vente enregistrée avec succès !')
            return render(request, 'vente/commandes.html')
    else:
        return render(request, 'vente/commandes.html')
