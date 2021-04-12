from django.shortcuts import render
from django.contrib import messages
from .forms import *
from .functions import *


# Create your views here.

def home(request):
    return render(request, 'personnel/main.html')


def insert_personnel(request):
    if request.method == "POST":
        personnel = PersonnelForm(request.POST, request.FILES)
        if personnel.is_valid():
            handle_cv(request.FILES['cv'])
            handle_photo(request.FILES['photo'])
            handle_contrat(request.FILES['contrat'])
            model_instance = personnel.save(commit=False)
            model_instance.save()
            messages.success(request, 'Le personnel a été enregistré avec succès !')
            return render(request, 'personnel/formulaire.html')
        else:
            messages.success(request, 'Il manque des données dans votre enregistrement !')
            return render(request, 'personnel/formulaire.html')

    else:
        return render(request, 'personnel/formulaire.html')


def liste_personnel(request):
    return render(request, 'personnel/liste_personnel.html')
