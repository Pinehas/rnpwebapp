from django import forms
from .models import *

class prodforms(forms.ModelForm):
    class Meta:
        model=ProduitModel
        fields="__all__"
