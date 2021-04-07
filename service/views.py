from django.shortcuts import render
from .models import *
from django.contrib import messages
from .forms import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'service/main.html')

def insert_service(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('marque') and request.POST.get('couleur'):
            saverecord=ServiceModel()
            saverecord.nom=request.POST.get('nom')
            saverecord.categorie = request.POST.get('categorie')
            saverecord.description = request.POST.get('description')
            saverecord.save()
            messages.success(request, 'Le Service a été enregistré avec succès !')
            return render(request, 'service/formulaire.html')
    else:
        return render(request, 'service/formulaire.html')

def details_service(request,id):
    obj=ServiceModel.objects.get(id=id)
    return render(request,'produit/details.html', {"ProduitModel":obj})

def editprod(request,id):
    obj=ServiceModel.objects.get(id=id)
    return render(request,'produit/edit_service.html', {"ProduitModel":obj})

def updateprod(request,id):
    modservice=ServiceModel.objects.get(id=id)
    form=serviceforms(request.POST, instance=modservice)
    if form.is_valid():
        form.save()
        messages.success(request, 'Le Service modifié avec succès !')

    return render(request,'produit/edit_service.html', {"data":modservice})
