
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),


    path('insert_projet', views.insert_projet, name="insert_projet"),

    path('delProjet/<int:id>/', views.delProjet, name="delProjet"),

    path('editprojet/<int:id>/', views.editprojet, name="editprojet"),

    path('lancement/<int:id>/', views.lancement, name="lancement"),
    

]
