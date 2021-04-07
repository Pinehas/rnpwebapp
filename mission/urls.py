
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('insert_mission', views.insert_mission, name="insert_mission"),
    path('insert_rapport', views.insert_rapport, name="insert_rapport"),
    path('delMission/<int:id>/', views.delMission, name="delMission"),

]
