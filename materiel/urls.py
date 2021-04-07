
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('sortie_materiel', views.sortie_materiel, name="sortie_materiel   "),
    path('insert_materiel', views.insert_materiel, name="insert_materiel"),

]
