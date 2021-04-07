from django import forms
from .models import PersonnelModel

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = PersonnelModel
        fields = "__all__"