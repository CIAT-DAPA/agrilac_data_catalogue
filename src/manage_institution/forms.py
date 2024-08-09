from django import forms
from .models import Institution

class InstitutionCreationForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'description', 'owner', 'is_certified']

class InstitutionChangeForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'description', 'owner', 'is_certified']
