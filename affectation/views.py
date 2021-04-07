from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .models import AffectationModel
from .forms import affectationforms
# Create your views here.

def home(request):
    return render(request, 'affectation/main.html')

def insert_affectation(request):
    if request.method=="POST":
        if request.POST.get('matricule') and request.POST.get('code_projet') and request.POST.get('date') and request.POST.get('details'):
            saverecord= AffectationModel()
            saverecord.matricule=request.POST.get('matricule')
            saverecord.code_projet = request.POST.get('code_projet')
            saverecord.date = request.POST.get('date')
            saverecord.details = request.POST.get('details')
            saverecord.save()
            messages.success(request, 'Affectation réussie !')
            return render(request, 'affectation/formulaire.html')
    else:
        return render(request, 'affectation/formulaire.html')



def editaffectation(request,id):
    editobj=AffectationModel.objects.get(id=id)
    return render(request,'affectation/edit_projet.html', {"AffectationModel":editobj})

def updateaffectation(request,id):
    modobj=AffectationModel.objects.get(id=id)
    form=affectationforms(request.POST, instance=modobj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Le Produit modifié avec succès !')

    return render(request,'affectation/edit_projet.html', {"AffectationModel":modobj})

def delaffectation(request,id):
    deleteobj=AffectationModel.objects.get(id=id)
    deleteobj.delete()
    showdata=AffectationModel.objects.all()
    return render(request, 'affectation/main.html', {"data":showdata})










def choix_personnel(request, id):
    obj= AffectationModel.object.get(id=id)
    return render(request, '', {"AffectationModel":obj})
def choix_projet(request, id):
    obj= AffectationModel.object.get(id=id)
    return render(request, '', {"AffectationModel":obj})
def details(request, id):
    obj= AffectationModel.object.get(id=id)
    return render(request, '', {"AffectationModel":obj})
def profil_personne(request, id):
    obj= AffectationModel.object.get(id=id)
    return render(request, '', {"AffectationModel":obj})
