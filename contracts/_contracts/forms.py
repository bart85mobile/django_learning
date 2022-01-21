from django import forms
from .models import ExternalEntity, InternalEntity, Contract

class ExternalEntityForm(forms.ModelForm):
    class Meta:
        model = ExternalEntity
        fields = ["company_name", "address", "address2", "city", "region", "postcode"]
        
class InternalEntityForm(forms.ModelForm):
    class Meta:
        model = InternalEntity
        fields = ["company_name", "address", "address2", "city", "region", "postcode"]
        
class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ["contract_name", "external_entity", "internal_entity", "contract_date", "contract_extension"]
