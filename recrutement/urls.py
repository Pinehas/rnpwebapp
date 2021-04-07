
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('insert_offre', views.insert_offre, name="insert_offre"),
    path('insert_demission', views.insert_demission, name="insert_demission"),
    path('insert_licenciement', views.insert_licenciement, name="insert_licenciement"),


]
