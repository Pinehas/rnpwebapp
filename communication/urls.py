
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('commentaire', views.commentaire, "commentaire"),
    path('contact', views.contact, name="contact"),
    path('contact', views.contact, name="contact"),
    path('insert_rep_client', views.insert_rep_client, name="insert_rep_client"),



]
