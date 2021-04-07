from django import forms
from .models import *

class serviceforms(forms.ModelForm):
    class Meta:
        model=ServiceModel
        fields="__all__"
