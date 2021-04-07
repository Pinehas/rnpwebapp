from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('MISSION')

def insert_mission(request):
    if request.method=="POST":
        if request.POST.get('id_personnel') and request.POST.get('objet') and request.POST.get('details') and request.POST.get('pays') and request.POST.get('ville') and request.POST.get('debut') and request.POST.get('fin'):
            saverecord=MissionModel()
            saverecord.id_personnel=request.POST.get('id_personnel')
            saverecord.objet = request.POST.get('objet')
            saverecord.details = request.POST.get('details')
            saverecord.pays = request.POST.get('pays')
            saverecord.ville = request.POST.get('ville')
            saverecord.debut = request.POST.get('debut')
            saverecord.fin = request.POST.get('fin')
            saverecord.save()
            messages.success(request, 'La mission a été enregistré avec succès !')
            return render(request, 'mission/formulaire.html')
    else:
        return render(request, 'mission/formulaire.html')

def insert_rapport(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('marque') and request.POST.get('couleur') and request.POST.get('categorie') and request.POST.get('variete') and request.POST.get('quantite') and request.POST.get('prix') and request.POST.get('descr'):
            saverecord=MissionModel()
            saverecord.nom=request.POST.get('nom')
            saverecord.couleur = request.POST.get('couleur')
            saverecord.categorie = request.POST.get('categorie')
            saverecord.variete = request.POST.get('variete')
            saverecord.marque = request.POST.get('marque')
            saverecord.quantite = request.POST.get('quantite')
            saverecord.prix = request.POST.get('prix')
            saverecord.descr = request.POST.get('descr')
            saverecord.save()
            messages.success(request, 'Le Produit '+saverecord.nom+' a été enregistré avec succès !')
            return render(request, 'mission/rapport.html')
    else:
        return render(request, 'mission/rapport.html')

def delMission(request,id):
    deleteprod=MissionModel.objects.get(id=id)
    deleteprod.delete()
    showdata=MissionModel.objects.all()
    return render(request, 'mission/main.html', {"data":showdata})


