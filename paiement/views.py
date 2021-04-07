from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'paiement/main.html')

def insert_paie_manoeuvre(request):
    if request.method=="POST":
        if request.POST.get('id_projet') and request.POST.get('travail') and request.POST.get('nom') and request.POST.get('no_cni') and request.POST.get('duree') and request.POST.get('salaire') and request.POST.get('date'):
            saverecord=PaiementManoeuvreModel()
            saverecord.id_projet=request.POST.get('id_projet')
            saverecord.travail = request.POST.get('travail')
            saverecord.nom = request.POST.get('nom')
            saverecord.no_cni = request.POST.get('no_cni')
            saverecord.duree = request.POST.get('duree')
            saverecord.salaire = request.POST.get('salaire')
            saverecord.date = request.POST.get('date')
            saverecord.save()
            messages.success(request, 'Le Paiement a été enregistré avec succès !')
            return render(request, 'paiement/form_manoeuvre.html')
    else:
        return render(request, 'paiement/form_manoeuvre.html')

def insert_achat(request):
    if request.method=="POST":
        if request.POST.get('id_projet') and request.POST.get('designation') and request.POST.get('objet') and request.POST.get('prix') and request.POST.get('quantite') and request.POST.get('date'):
            saverecord=AchatModel()
            saverecord.id_projet=request.POST.get('id_projet')
            saverecord.designation = request.POST.get('designation')
            saverecord.objet = request.POST.get('objet')
            saverecord.prix = request.POST.get('prix')
            saverecord.quantite = request.POST.get('quantite')
            saverecord.date = request.POST.get('date')
            saverecord.save()
            messages.success(request, 'L''achat a été enregistré avec succès !')
            return render(request, 'paiement/form_achat.html')
    else:
        return render(request, 'paiement/form_achat.html')


def insert_paie_sortant(request):
    if request.method=="POST":
        if request.POST.get('id_projet') and request.POST.get('sujet') and request.POST.get('objet') and request.POST.get('details') and request.POST.get('montant') and request.POST.get('date'):
            saverecord=PaiementSortantModel()
            saverecord.id_projet=request.POST.get('id_projet')
            saverecord.sujet = request.POST.get('sujet')
            saverecord.objet = request.POST.get('objet')
            saverecord.details = request.POST.get('details')
            saverecord.montant = request.POST.get('montant')
            saverecord.date = request.POST.get('date')
            saverecord.save()
            messages.success(request, 'Le Paiement a été enregistré avec succès !')
            return render(request, 'paiement/form_paiement_sortant.html')
    else:
        return render(request, 'paiement/form_paiement_sortant.html')


def insert_paie_entrant(request):
    if request.method=="POST":
        if request.POST.get('id_projet') and request.POST.get('nature') and request.POST.get('details') and request.POST.get('montant') and request.POST.get('montant_restant') and request.POST.get('date'):
            saverecord=PaiementEntrantModel()
            saverecord.id_projet=request.POST.get('id_projet')
            saverecord.nature = request.POST.get('nature')
            saverecord.details = request.POST.get('details')
            saverecord.montant = request.POST.get('montant')
            saverecord.montant_restant = request.POST.get('montant_restant')
            saverecord.date = request.POST.get('date')
            saverecord.descr = request.POST.get('descr')
            saverecord.save()
            messages.success(request, 'Le Paiement a été enregistré avec succès !')
            return render(request, 'paiement/form_paiement_entrant.html')
    else:
        return render(request, 'paiement/form_paiement_entrant.html')

def insert_credit(request):
    if request.method=="POST":
        if request.POST.get('origine') and request.POST.get('objet') and request.POST.get('details') and request.POST.get('montant') and request.POST.get('date_remboursement') and request.POST.get('date'):
            saverecord=CreditModel()
            saverecord.origine=request.POST.get('origine')
            saverecord.objet = request.POST.get('objet')
            saverecord.details = request.POST.get('details')
            saverecord.montant = request.POST.get('montant')
            saverecord.date_remboursement = request.POST.get('date_remboursement')
            saverecord.date = request.POST.get('date')
            saverecord.save()
            messages.success(request, 'Le Credit a été enregistré avec succès !')
            return render(request, 'paiement/form_credit.html')
    else:
        return render(request, 'paiement/form_credit.html')


def insert_rembourssement(request):
    if request.method=="POST":
        if request.POST.get('id_credit') and request.POST.get('nature') and request.POST.get('details') and request.POST.get('montant') and request.POST.get('montant_restant') and request.POST.get('date'):
            saverecord=RemboursementModel()
            saverecord.id_credit=request.POST.get('id_credit')
            saverecord.nature = request.POST.get('nature')
            saverecord.details = request.POST.get('details')
            saverecord.montant = request.POST.get('montant')
            saverecord.montant_restant = request.POST.get('montant_restant')
            saverecord.date = request.POST.get('date')
            saverecord.save()
            messages.success(request, 'Le rembourssement a été enregistré avec succès !')
            return render(request, 'paiement/form_rembourssement.html')
    else:
        return render(request, 'paiement/form_rembourssement.html')
def insert_capital(request):
    if request.method=="POST":
        if request.POST.get('origine') and request.POST.get('objet') and request.POST.get('details') and request.POST.get('montant') and request.POST.get('date'):
            saverecord=CapitalModel()
            saverecord.origine=request.POST.get('origine')
            saverecord.objet = request.POST.get('objet')
            saverecord.details = request.POST.get('details')
            saverecord.montant = request.POST.get('montant')
            saverecord.date = request.POST.get('date')
            saverecord.save()
            messages.success(request, 'Le Capital a été enregistré avec succès !')
            return render(request, 'paiement/form_capital.html')
    else:
        return render(request, 'paiement/form_capital.html')




