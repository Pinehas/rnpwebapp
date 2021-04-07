
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),


    path('insert_conges', views.insert_conges, name="insert_conges"),
    path('suppr_conges', views.suppr_conges, name="suppr_conges"),

]
