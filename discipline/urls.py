
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('liste_disc', views.liste_disc, name="liste_disc"),
    path('liste_expl', views.liste_expl, name="liste_expl"),
    path('insert_disc', views.insert_disc, name="insert_disc"),
    path('liste_expl', views.liste_expl, name="liste_expl"),
]
