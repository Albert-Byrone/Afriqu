from django import forms
from .models import *

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        exclude = ['date']

class UseMaterialForm(forms.ModelForm):
    class Meta:
        model = Usematerial
        exclude = ['date']