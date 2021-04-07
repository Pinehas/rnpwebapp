
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),


    path('insert_affectation', views.insert_affectation, name="insert_affectation"),
    path('editaffectation/<int:id>/', views.editaffectation, name="editaffectation"),
    path('modaffectation/<int:id>/', views.updateaffectation, name="modaffectation"),
    path('supraffectation/<int:id>/', views.delaffectation, name="supraffectation"),
    path('choix_personnel/<int:id>/', views.choix_personnel, name="choix_personnel"),
    path('choix_projet/<int:id>/', views.choix_projet, name="choix_projet"),
    path('details/<int:id>/', views.details, name="details"),
    path('profil_personnel/<int:id>/', views.profil_personne, name="profil_personnel"),

]
