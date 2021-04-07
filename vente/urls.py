
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('insert_vente', views.insert_vente, name="insert_vente"),

]
