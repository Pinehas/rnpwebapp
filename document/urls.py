
from django.urls import path
from document import views

urlpatterns = [
    path('', views.home),

    path('insert_doc', views.insert_doc, name="insert_doc"),

]
