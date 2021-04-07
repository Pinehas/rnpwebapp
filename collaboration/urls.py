
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),

    path('details_conf/<int:id>/', views.details_conf,"details_conf"),
    path('presence', views.presence, name="presence"),
    path('ecrire', views.ecrire, name="ecrire"),
    path('insert_annonce', views.insert_annonce, name="insert_annonce"),
    path('insert_note', views.insert_note, name="insert_note"),

    path('inviter', views.inviter,"inviter"),
    path('insert_conference', views.insert_conference, name="insert_conference"),
    path('presence/<int:id>/', views.presence, name="presence"),
    path('rapport', views.rapport, name="rapport"),
    path('conferences', views.conferences, name="conferences"),

    path('notes', views.notes,"notes"),
    path('annonces', views.annonces, "annonces"),
    path('supprimer_conf/<int:id>/', views.supprimer_conf, name="supprimer_conf"),
    path('supprimer_invite/<int:id>/', views.supprimer_invite, name="supprimer_invite"),


]
