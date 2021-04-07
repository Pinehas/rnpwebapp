
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('insert_personnel', views.insert_personnel, name="insert_personnel"),
    path('liste_personnel', views.liste_personnel, name="liste_personnel"),

    

]
