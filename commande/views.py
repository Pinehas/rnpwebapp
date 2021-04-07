from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    showcmd=Cmd_Prod_Model.objects.all()
    showdmd=Dmd_Serv_Model.objects.all()
    return render(request, 'commande/main.html', {"dmd":showdmd, "cmd":showcmd})

def list_cmd(request):
    showcmd=Cmd_Prod_Model.objects.all()
    return render(request, 'commande/cmd_produits.html', {"cmd":showcmd})

def list_dmd(request):
    showdmd=Dmd_Serv_Model.objects.all()
    return render(request, 'commande/dmd_services.html', {"dmd":showdmd})

def insert_cmd(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('marque') and request.POST.get('couleur') and request.POST.get('categorie')\
                and request.POST.get('variete') and request.POST.get('quantite') and request.POST.get('prix') and request.POST.get('descr'):
            saverecord=Cmd_Prod_Model()
            saverecord.nom=request.POST.get('nom')
            saverecord.couleur = request.POST.get('couleur')
            saverecord.categorie = request.POST.get('categorie')
            saverecord.variete = request.POST.get('variete')
            saverecord.marque = request.POST.get('marque')
            saverecord.quantite = request.POST.get('quantite')
            saverecord.prix = request.POST.get('prix')
            saverecord.descr = request.POST.get('descr')
            saverecord.save()
            messages.success(request, 'Commande de produit enregistrée avec succès !')
            return render(request, 'commande/form_cmd.html')
    else:
        return render(request, 'commande/form_cmd.html')

def insert_dmd(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('marque') and request.POST.get('couleur') and request.POST.get('categorie')\
                and request.POST.get('variete') and request.POST.get('quantite') and request.POST.get('prix') and request.POST.get('descr'):
            saverecord=Dmd_Serv_Model()
            saverecord.nom=request.POST.get('nom')
            saverecord.couleur = request.POST.get('couleur')
            saverecord.categorie = request.POST.get('categorie')
            saverecord.variete = request.POST.get('variete')
            saverecord.marque = request.POST.get('marque')
            saverecord.quantite = request.POST.get('quantite')
            saverecord.prix = request.POST.get('prix')
            saverecord.descr = request.POST.get('descr')
            saverecord.save()
            messages.success(request, 'Demande de service enregistrée avec succès !')
            return render(request, 'commande/form_dmd.html')
    else:
        return render(request, 'commande/form_dmd.html')





def editcmd(request,id):
    cmd=Cmd_Prod_Model.objects.get(id=id)
    return render(request,'commande/edit_cmd.html', {"cmd":cmd})

def details_cmd(request,id):
    cmd=Cmd_Prod_Model.objects.get(id=id)
    return render(request,'commande/details _cmd.html', {"cmd":cmd})

def updatecmd(request,id):
    modcmd=Cmd_Prod_Model.objects.get(id=id)
    form=cmdforms(request.POST, instance=modcmd)
    if form.is_valid():
        form.save()
        messages.success(request, 'Le Produit modifié avec succès !')

    return render(request,'commande/edit_cmd.html', {"cmd":modcmd})

def delcmd(request,id):
    deletecmd=Cmd_Prod_Model.objects.get(id=id)
    deletecmd.delete()
    showcmd=Cmd_Prod_Model.objects.all()
    return render(request, 'commande/cmd_produits.html', {"cmd":showcmd})



def editdmd(request,id):
    dmd=Dmd_Serv_Model.objects.get(id=id)
    return render(request,'commande/edit_dmd.html', {"dmd":dmd})

def details_dmd(request,id):
    dmd=Dmd_Serv_Model.objects.get(id=id)
    return render(request,'commande/details _dmd.html', {"dmd":dmd})

def updatedmd(request,id):
    moddmd=Dmd_Serv_Model.objects.get(id=id)
    form=dmdforms(request.POST, instance=moddmd)
    if form.is_valid():
        form.save()
        messages.success(request, 'Le Produit modifié avec succès !')

    return render(request,'commande/edit_dmd.html', {"dmd":moddmd})

def deldmd(request,id):
    deletedmd=Dmd_Serv_Model.objects.get(id=id)
    deletedmd.delete()
    showdmd=Dmd_Serv_Model.objects.all()
    return render(request, 'commande/dmd_services.html', {"dmd":showdmd})


