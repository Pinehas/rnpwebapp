from django import forms
from .models import Cmd_Prod_Model, Dmd_Serv_Model

class cmdforms(forms.ModelForm):
    class Meta:
        model= Cmd_Prod_Model
        fields="__all__"

class dmdforms(forms.ModelForm):
    class Meta:
        model= Dmd_Serv_Model
        fields="__all__"
