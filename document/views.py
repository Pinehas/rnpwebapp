from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    showdata = DocumentModel.objects.all()
    return render(request, 'produit/index.html', {"data": showdata})

def insert_doc(request):
    if request.method=="POST":
        if request.POST.get('titre') and request.POST.get('categorie') and request.POST.get('description') and request.POST.get('acces') and request.POST.get('document') and request.POST.get('date_ajout'):
            saverecord=DocumentModel()
            saverecord.titre=request.POST.get('titre')
            saverecord.categorie = request.POST.get('categorie')
            saverecord.description = request.POST.get('description')
            saverecord.acces = request.POST.get('acces')
            saverecord.document = request.POST.get('document')
            saverecord.date_ajout = request.POST.get('date_ajout')
            saverecord.save()
            messages.success(request, 'Document enregistré avec succès !')
            return render(request, 'document/formulaire.html')
    else:
        return render(request, 'document/formulaire.html')

def deldoc(request,id):
    deletedoc=DocumentModel.objects.get(id=id)
    deletedoc.delete()
    showdata = DocumentModel.objects.all()
    return render(request, 'document/main.html', {"data":showdata})


