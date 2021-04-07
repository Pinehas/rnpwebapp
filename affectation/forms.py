from django import forms
from .models import AffectationModel


class affectationforms(forms.ModelForm):
    class Meta:
        model=AffectationModel
        fields="__all__"
