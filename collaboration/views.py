from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'collaboration/main.html')

def insert_conference(request):
    if request.method=="POST":
        if request.POST.get('objet') and request.POST.get('frequence') and request.POST.get('participant') and request.POST.get('date') and request.POST.get('heure'):
            saverecord=ConferenceModel()
            saverecord.objet=request.POST.get('objet')
            saverecord.frequence = request.POST.get('frequence')
            saverecord.date = request.POST.get('date')
            saverecord.heure = request.POST.get('heure')
            saverecord.save()
            messages.success(request, 'Conférence Ajoutée !')
            return render(request, 'collaboration/formulaire.html')
    else:
        return render(request, 'collaboration/formulaire.html')

def inviter(request):
    if request.method=="POST":
        if request.POST.get('id_conference') and request.POST.get('id_personnel'):
            saverecord = InvitationModel()
            saverecord.id_conference =request.POST.get('id_conference')
            saverecord.id_personnel = request.POST.get('id_personnel')
            saverecord.save()
            messages.success(request, 'Invité !')
            return render(request, 'collaboration/invitation.html')
    else:
        return render(request, 'collaboration/invitation.html')

def ecrire(request):
    if request.method=="POST":
        if request.POST.get('id_conference') and request.POST.get('id_personnel') and request.POST.get('id_cible') and request.POST.get('id_texte'):
            saverecord = InvitationModel()
            saverecord.id_conference =request.POST.get('id_conference')
            saverecord.id_personnel = request.POST.get('id_personnel')
            saverecord.id_cible =request.POST.get('id_cible')
            saverecord.texte = request.POST.get('texte')
            saverecord.save()
            return render(request, 'collaboration/reunion.html')
    else:
        return render(request, 'collaboration/reunion.html')


def insert_annonce(request):
    if request.method=="POST":
        if request.POST.get('id_conference') and request.POST.get('id_personnel') and request.POST.get('id_cible') and request.POST.get('id_texte'):
            saverecord = AnnonceModel()
            saverecord.objet =request.POST.get('objet')
            saverecord.texte = request.POST.get('texte')
            saverecord.save()
            return render(request, 'collaboration/reunion.html')
    else:
        return render(request, 'collaboration/reunion.html')

def insert_note(request):
    if request.method=="POST":
        if request.POST.get('id_conference') and request.POST.get('id_personnel') and request.POST.get('id_cible') and request.POST.get('id_texte'):
            saverecord = NoteModel()
            saverecord.type_note =request.POST.get('type_note')
            saverecord.texte = request.POST.get('texte')
            saverecord.save()
            return render(request, 'collaboration/reunion.html')
    else:
        return render(request, 'collaboration/reunion.html')


def details_conf(request,id):
    show = InvitationModel.objects.get(id_conference=id)
    return render(request,'collaboration/invitation.html', {"data":show})


def presence(request,id):
    show = PresenceModel.objects.get(id_conference=id)
    return render(request,'collaboration/presence.html', {"data":show})

def rapport(request):
    showall = ConferenceModel.objects.all()
    return render(request, 'collaboration/rapport.html',{"data":showall})

def conferences(request):
    showall = ConferenceModel.objects.all()
    return render(request, 'collaboration/conferences.html',{"data":showall})

def supprimer_conf(request,id):
    delete=ConferenceModel.objects.get(id=id)
    delete.delete()
    showdata=ConferenceModel.objects.all()
    return render(request, 'collaboration/conferences.html', {"data":showdata})

def supprimer_invite(id):
    delete=InvitationModel.objects.get(id=id)
    delete.delete()


def notes(request):
    showall = NoteModel.objects.all()
    return render(request, 'collaboration/notes.html',{"data":showall})

def annonces(request):
    showall = AnnonceModel.objects.all()
    return render(request, 'collaboration/annonces.html',{"data":showall})
