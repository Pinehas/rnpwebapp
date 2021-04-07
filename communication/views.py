from django.shortcuts import render
from django.contrib import messages
from .models import *
from client.models import ReponseClientModel, MessageClientModel
# Create your views here.

def home(request):
    liste_commentaires = CommentaireModel.objects.all()
    liste_contacts = ContactModel.objects.all()
    return render(request, 'communication/main.html', {"comment":liste_commentaires, "contact":liste_contacts})



def commentaire(request):
    showall = CommentaireModel.objects.all()
    return render(request, 'communication/commentaires.html',{"data":showall})

def contact(request):
    showall = ContactModel.objects.all()
    return render(request, 'communication/contacts.html',{"data":showall})


def inbox(request):
    showmsg = ReponseClientModel.objects.all()
    showrep = MessageClientModel.objects.all()
    return render(request, 'communication/inbox.html',{"msg":showmsg, "rep":showrep})

def insert_rep_client(request):
    if request.method=="POST":
        if request.POST.get('id_client') and request.POST.get('message'):
            saverecord=ReponseClientModel()
            saverecord.id_client =request.POST.get('id_client')
            saverecord.message = request.POST.get('message')
            saverecord.save()
            messages.success(request, 'Message envoyé !')
            showmsg = ReponseClientModel.objects.all()
            showrep = MessageClientModel.objects.all()
            return render(request, 'communication/inbox.html',{"msg":showmsg, "rep":showrep})
    else:
        showmsg = ReponseClientModel.objects.all()
        showrep = MessageClientModel.objects.all()
        return render(request, 'communication/inbox.html',{"msg":showmsg, "rep":showrep})
