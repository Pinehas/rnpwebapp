
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('insert_permission', views.insert_permission, name="insert_permission"),

]
