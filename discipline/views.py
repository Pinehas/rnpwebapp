from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    cas_disc = DisciplineModel.objects.all()
    cas_expl = ExplicationModel.objects.all()
    return render(request, 'discipline/main.html', {"data_disc": cas_disc, "data_expl": cas_expl})

def liste_disc(request):
    cas_disc = DisciplineModel.objects.all()
    return render(request, 'discipline/discipline.html', {"data_disc": cas_disc})

def liste_expl(request):
    cas_expl = ExplicationModel.objects.all()
    return render(request, 'discipline/explication.html', {"data_expl": cas_expl})

def insert_disc(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('objet') and request.POST.get('details'):
            saverecord=DisciplineModel()
            saverecord.nom=request.POST.get('nom')
            saverecord.couleur = request.POST.get('objet')
            saverecord.categorie = request.POST.get('details')
            saverecord.save()
            messages.success(request, 'Element Ajouté avec succès!')
            return render(request, 'discipline/form_discipline.html')
    else:
        return render(request, 'discipline/form_discipline.html')

def insert_expl(request):
    if request.method=="POST":
        if request.POST.get('id_discipline') and request.POST.get('nom') and request.POST.get('objet') and request.POST.get('details'):
            saverecord = DisciplineModel()
            saverecord.nom = request.POST.get('nom')
            saverecord.couleur = request.POST.get('objet')
            saverecord.categorie = request.POST.get('details')
            saverecord.save()
            messages.success(request, 'Element ajouté avec succès !')
            return render(request, 'discipline/form_explication.html')
    else:
        return render(request, 'discipline/form_explication.html')

