
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('login', views.login, name="login"),
    path('services', views.services, name="services"),
    path('produits', views.produits, name="produits"),
    path('candidature', views.candidature, name="candidature"),
    path('postuler', views.postuler, name="postuler"),
    path('insert_candidat', views.insert_candidat, name="insert_candidat"),
    path('message', views.message, name="message"),
    path('offres', views.offres, name="offres"),

    path('insert_commentaire', views.insert_commentaire, "insert_commentaire"),
    path('insert_contact', views.insert_contact, name="insert_contact"),

    
    path('details_produit/<int:id>/', views.details_produit, name="details_produit"),
    path('details_service/<int:id>/', views.details_service, name="details_service"),
    path('details_offre/<int:id>/', views.details_offre, name="details_offre"),
]
