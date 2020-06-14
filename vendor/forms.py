from django.forms import ModelForm
from django import forms
from .models import Vendor


class VendorForm(ModelForm):
    class Meta:
        model= Vendor
        fields = ['name','cnpj','city']

        widgets = {
                    'cnpj': forms.TextInput(attrs={'class':'form-control','placeholder':'99.999.999/9999-99'}),
                   }