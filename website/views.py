from django.shortcuts import render
from produit.models import *
from communication.models import *
from service.models import *
from recrutement.models import CandidatModel
from recrutement.models import OffreModel
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'website/index.html')

def contact(request):
    return render(request, 'website/contact.html')

def about(request):
    return render(request, 'website/about.html')

def login(request):
    return render(request, 'website/login.html')

def services(request):
    service = ServiceModel.objects.all()
    return (request, 'website/services.html',{"data":service})

def produits(request):
    produit = ProduitModel.objects.all()
    return render(request, 'website/produits.html',{"data":produit})

def candidature(request):
    return render(request, 'website/candidature.html')

def postuler(request):
    return render(request, 'website/postuler.html')

def message(request):
    return render(request, 'website/message.html')


def offres(request):
    job = OffreModel.objects.all()
    return render(request, 'website/offres.html',{"data":job})

def insert_candidat(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('poste') and request.POST.get('specialite') and request.POST.get('niveau') and request.POST.get('experience')\
                and request.POST.get('pays') and request.POST.get('ville') and request.POST.get('motivation'):
            saverecord=CandidatModel()
            saverecord.nom=request.POST.get('nom')
            saverecord.poste = request.POST.get('poste')
            saverecord.specialite = request.POST.get('specialite')
            saverecord.niveau = request.POST.get('niveau')
            saverecord.experience = request.POST.get('experience')
            saverecord.pays = request.POST.get('pays')
            saverecord.ville = request.POST.get('ville')
            saverecord.motivation = request.POST.get('motivation')
            saverecord.save()
            messages.success(request, 'Votre candidature a été enregistré avec succès !')
            return render(request, 'website/postuler.html')
    else:
        return render(request, 'website/postuler.html')


def details_produit(request, id):
    produit = ProduitModel.objects.get(id=id)
    return render(request, 'website/detail_produit.html',{"data":produit})
def details_service(request, id):
    service = ServiceModel.objects.get(id=id)
    return render(request, 'website/detail_service.html',{"data":service})
def details_offre(request, id):
    job = OffreModel.objects.get(id=id)
    return render(request, 'website/detail_offre.html',{"data":job})


def insert_commentaire(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('email') and request.POST.get('objet') and request.POST.get('message'):
            saverecord=CommentaireModel()
            saverecord.nom=request.POST.get('nom')
            saverecord.email = request.POST.get('email')
            saverecord.message = request.POST.get('message')
            saverecord.save()
            messages.success(request, 'Message envoyé !')
            return render(request, 'website/message.html')
    else:
        return render(request, 'website/message.html')

def insert_contact(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('email') and request.POST.get('objet') and request.POST.get('message'):
            saverecord=CommentaireModel()
            saverecord.nom=request.POST.get('nom')
            saverecord.email = request.POST.get('email')
            saverecord.objet = request.POST.get('objet')
            saverecord.message = request.POST.get('message')
            saverecord.save()
            messages.success(request, 'Message envoyé !')
            return render(request, 'website/message.html')
    else:
        return render(request, 'website/message.html')
