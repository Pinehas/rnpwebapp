from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),


    path('insert_client', views.insert_client, name="insert_client"),
    path('insert_msg_client', views.insert_msg_client, name="insert_msg_client"),


]
