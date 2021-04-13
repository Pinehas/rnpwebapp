from django.shortcuts import render
from .models import *
from .forms import *
from .functions import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.



def home(request):
    return render(request, 'client/main.html')

def insert_client(request):

    if request.method=="POST":
        form = ClientModel()
        if request.FILES['photo']:
            form.nom=request.POST.get('nom')
            form.categorie = request.POST.get('categorie')
            form.telephone = request.POST.get('telephone')
            form.email = request.POST.get('email')
            form.pays = request.POST.get('pays')
            form.ville = request.POST.get('ville')
            form.quartier = request.POST.get('quartier')
            form.img_client = request.FILES['photo']
            form.password = request.POST.get('password')
            form.save()
            messages.success(request, 'Inscription réussie ! Veillez vous connecter svp')
                #return render(request, 'website/register.html')
            #messages.success(request, 'FORMULAIRE NON ENREGISTRE !')
            return render(request, 'website/register.html')


        else:
            messages.success(request, 'Echec de l''inscription !')
            return render(request, 'website/register.html')
    else:
        return render(request, 'website/register.html')

def insert_msg_client(request):
    if request.method=="POST":
        if request.POST.get('id_client') and request.POST.get('message'):
            saverecord=MessageClientModel()
            saverecord.id_client =request.POST.get('id_client')
            saverecord.message = request.POST.get('message')
            saverecord.save()
            messages.success(request, 'Message envoyé !')
            return render(request, 'client/inbox.html')
    else:
        return render(request, 'client/inbox.html')


