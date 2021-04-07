
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('insert_service', views.insert_service, name="insert_service"),
    path('detail_service/<int:id>/', views.details_service, name="details_service"),

]
