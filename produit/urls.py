
from django.urls import path
from . import views
app_name = 'produit'
urlpatterns = [
    path('', views.home, name="produits"),
    path('insert_produit', views.insert_produit, name="insert_produit"),
    path('editprod/<int:id>/', views.editprod, name="editprod"),
    path('modprod/<int:id>/', views.updateprod, name="modprod"),
    path('supprod/<int:id>/', views.updateprod, name="supprod"),
    path('detail_produit/<int:id>/', views.details_produit, name="details_produit"),
]
