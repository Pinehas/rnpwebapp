
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('insert_paie_manoeuvre', views.insert_paie_manoeuvre, name="insert_paie_manoeuvre"),
    path('insert_achat', views.insert_achat, name="insert_achat"),
    path('insert_paie_sortant', views.insert_paie_sortant, name="insert_paie_sortant"),
    path('insert_paie_entrant', views.insert_paie_entrant, name="insert_paie_entrant"),
    path('insert_credit', views.insert_credit, name="insert_credit"),
    path('insert_rembourssement', views.insert_rembourssement, name="insert_rembourssement"),
    path('insert_capital', views.insert_capital, name="insert_capital"),


]
