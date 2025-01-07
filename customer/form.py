from django import forms
from django.core.exceptions import ValidationError

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'addressline1', 'city', 'postcode',
                  'country', 'active', 'creditlimit', 'notes')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'addressline1': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode':  forms.TextInput(attrs={'class': 'form-control'}),
            'country':  forms.TextInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(),
            'creditlimit': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }
        labels = {
            'notes': 'Place notes here:',
            'active': 'Status (Active)',
            'addressline1': 'Address'
        }

    def clean_creditlimit(self):
        creditlimit = self.cleaned_data['creditlimit']
        if creditlimit > 15000:
            raise ValidationError("Credit Limit must be less than $15,000!")
        return creditlimit

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) == 0:
            raise ValidationError("Name is required.")
        return name
