
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('insert_salaire', views.insert_salaire, name="insert_salaire"),

]
