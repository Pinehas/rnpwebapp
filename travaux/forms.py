from django import forms

from .models import *

class projetforms(forms.ModelForm):
    class Meta:
        model=ProjetModel
        fields="__all__"
