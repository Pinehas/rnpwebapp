"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('website.urls')),
    path('affectation/', include('affectation.urls')),
    path('client/', include('client.urls')),
    path('commande/', include('commande.urls')),
    path('collaboration./', include('collaboration.urls')),
    path('communication/', include('communication.urls')),
    path('conges/', include('conges.urls')),
    path('discipline/', include('discipline.urls')),
    path('document/', include('document.urls')),
    path('materiel/', include('materiel.urls')),
    path('mission/', include('mission.urls')),
    path('paiement/', include('paiement.urls')),
    path('permission/', include('permission.urls')),
    path('personnel/', include('personnel.urls')),
    path('produit/', include('produit.urls')),
    path('recrutement/', include('recrutement.urls')),
    path('salaire/', include('salaire.urls')),
    path('service/', include('service.urls')),
    path('travaux/', include('travaux.urls')),
    path('vente/', include('vente.urls')),

]
