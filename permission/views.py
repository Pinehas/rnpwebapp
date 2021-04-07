from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'permission/main.html')

def insert_permission(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('marque') and request.POST.get('couleur') and request.POST.get('categorie') and request.POST.get('variete') and request.POST.get('quantite') and request.POST.get('prix') and request.POST.get('descr'):
            saverecord=PermissionModel()
            saverecord.id_personnel=request.POST.get('id_personnel')
            saverecord.service = request.POST.get('service')
            saverecord.poste = request.POST.get('poste')
            saverecord.motif = request.POST.get('motif')
            saverecord.duree = request.POST.get('duree')
            saverecord.save()
            messages.success(request, 'La Permission a été enregistré avec succès !')
            return render(request, 'permission/formulaire.html')
    else:
        return render(request, 'permission/formulaire.html')
