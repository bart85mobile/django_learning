from django import forms
from .models import BusinessEntity

class BusinessEntityForm(forms.ModelForm):
    class Meta:
        model = BusinessEntity
        fields = ["company_name", "company_type", "address", "address2", "city", "region", "postcode"]