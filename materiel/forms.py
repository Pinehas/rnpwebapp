from django import forms
from produit.models import ProduitModel

class prodforms(forms.ModelForm):
    class Meta:
        model=ProduitModel
        fields="__all__"
