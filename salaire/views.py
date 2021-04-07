from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'salaire/main.html')


def insert_salaire(request):
    if request.method=="POST":
        if request.POST.get('id_personnel') and request.POST.get('montant') and request.POST.get('date'):
            saverecord=SalaireModel()
            saverecord.id_personnel=request.POST.get('id_personnel')
            saverecord.montant = request.POST.get('montant')
            saverecord.date = request.POST.get('date')
            saverecord.save()
            messages.success(request, 'Paiement de Salaire a été enregistré avec succès !')
            return render(request, 'salaire/formulaire.html')
    else:
        return render(request, 'salaire/formulaire.html')
