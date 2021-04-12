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
        client = ClientForm(request.POST, request.FILES)
        if client.is_valid():
            handle_img_client(request.FILES['photo'])
            model_instance = client.save(commit=False)
            model_instance.save()
            messages.success(request, 'Inscription réussie ! Connectez-vous s''il vous plaît !')
            return render(request, 'website/register.html')
        else:
            messages.success(request, 'echec de l''inscription !')
            return render(request, 'website/register.html')


#        if request.POST.get('nom') and request.POST.get('categorie') and request.POST.get('telephone') and request.POST.get('email')  and request.POST.get('pays') and request.POST.get('ville') and request.POST.get('quartier') and request.POST.get('photo') and request.POST.get('password'):

#            saverecord=ClientModel()
#            saverecord.nom=request.POST.get('nom')
#            saverecord.categorie = request.POST.get('categorie')
#            saverecord.telephone = request.POST.get('telephone')
#            saverecord.email = request.POST.get('email')
#            saverecord.pays = request.POST.get('pays')
#            saverecord.ville = request.POST.get('ville')
#            saverecord.quartier = request.POST.get('quartier')
#            saverecord.photo = request.POST.get('photo')
#            saverecord.password = request.POST.get('password')
#            saverecord.save()
#            messages.success(request, 'Inscription réussie ! Veillez vous connecter svp')
#            return render(request, 'website/register.html')
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


