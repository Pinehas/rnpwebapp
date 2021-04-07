from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    showdata = MaterielModel.objects.all()
    return render(request, 'materiel/main.html', {"data": showdata})

def insert_materiel(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('categorie') and request.POST.get('quantite') and request.POST.get('prix') and request.POST.get('marque') and request.POST.get('couleur') and request.POST.get('variete') and request.POST.get('guide') and request.POST.get('descr'):
            saverecord=MaterielModel()
            saverecord.nom=request.POST.get('nom')
            saverecord.categorie = request.POST.get('categorie')
            saverecord.quantite = request.POST.get('quantite')
            saverecord.prix = request.POST.get('prix')
            saverecord.marque = request.POST.get('marque')
            saverecord.couleur = request.POST.get('couleur')
            saverecord.variete = request.POST.get('variete')
            saverecord.guide = request.POST.get('guide')
            saverecord.descr = request.POST.get('descr')
            saverecord.save()
            messages.success(request, 'Le materiel a été enregistré avec succès !')
            return render(request, 'materiel/formulaire.html')
    else:
        return render(request, 'materiel/formulaire.html')

def sortie_materiel(request,id):
        sortie = MaterielModel.objects.get(id=id)
        return render(request, 'materiel/form_sortie.html', {"data":sortie})


def delmat(request,id):
    deletemat=MaterielModel.objects.get(id=id)
    deletemat.delete()
    showdata=MaterielModel.objects.all()
    return render(request, 'materiel/main.html', {"data":showdata})


