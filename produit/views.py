from django.contrib import messages
from django.shortcuts import render
from produit.models import ProduitModel
from produit.forms import prodforms

# Create your views here.

def home(request):
    showall = ProduitModel.objects.all()
    return render(request, 'produit/index.html',{"data":showall})

def insert_produit(request):
    if request.method=="POST":
        if request.POST.get('nom') and request.POST.get('marque') and request.POST.get('couleur') and request.POST.get('categorie') and request.POST.get('variete') and request.POST.get('quantite') and request.POST.get('prix') and request.POST.get('descr'):
            saverecord=ProduitModel()
            saverecord.nom=request.POST.get('nom')
            saverecord.couleur = request.POST.get('couleur')
            saverecord.categorie = request.POST.get('categorie')
            saverecord.variete = request.POST.get('variete')
            saverecord.marque = request.POST.get('marque')
            saverecord.quantite = request.POST.get('quantite')
            saverecord.prix = request.POST.get('prix')
            saverecord.descr = request.POST.get('descr')
            saverecord.save()
            messages.success(request, 'Le Produit '+saverecord.nom+' a été enregistré avec succès !')
            return render(request, 'produit/formulaire.html')
    else:
        return render(request, 'produit/formulaire.html')





def editprod(request,id):
    editprodobj=ProduitModel.objects.get(id=id)
    return render(request,'produit/edit_produit.html', {"ProduitModel":editprodobj})

def details_produit(request,id):
    obj=ProduitModel.objects.get(id=id)
    return render(request,'produit/details.html', {"ProduitModel":obj})

def updateprod(request,id):
    modprod=ProduitModel.objects.get(id=id)
    form=prodforms(request.POST, instance=modprod)
    if form.is_valid():
        form.save()
        messages.success(request, 'Le Produit modifié avec succès !')

    return render(request,'produit/edit_produit.html', {"ProduitModel":modprod})

def delProd(request,id):
    deleteprod=ProduitModel.objects.get(id=id)
    deleteprod.delete()
    showdata=ProduitModel.objects.all()
    return render(request, 'produit/main.html', {"data":showdata})


