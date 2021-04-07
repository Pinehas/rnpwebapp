from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    liste_conges = CongesModel.objects.all()
    return render(request, 'conges/main.html', {"data":liste_conges})

def insert_conges(request):
    if request.method=="POST":
        if request.POST.get('id_personnel') and request.POST.get('debut') and request.POST.get('fin'):
            saverecord=CongesModel()
            saverecord.id_personnel = request.POST.get('id_personnel')
            saverecord.debut = request.POST.get('debut')
            saverecord.fin = request.POST.get('fin')
            saverecord.save()
            messages.success(request, 'Conges ajouté avec succès !')
            return render(request, 'conges/formulaire.html')
    else:
        return render(request, 'conges/formulaire.html')

def suppr_conges(request,id):
    deletting=CongesModel.objects.get(id=id)
    deletting.delete()
    showdata=CongesModel.objects.all()
    return render(request, 'conges/main.html', {"data":showdata})

