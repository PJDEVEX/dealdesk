from django import forms
from .models import Client, CLIENT_TYPE_CHOICES
from team.models import Sar


class ClientFilterForm(forms.Form):
    """
    Filter form for filtering clients
    """
    client_type = forms.ChoiceField(
        choices=[('', 'All')] + list(CLIENT_TYPE_CHOICES),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    salesman = forms.ModelChoiceField(
        queryset=Sar.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
        )
    
    search_keyword = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )


class ClientForm(forms.ModelForm):
    """
    Form for creating and updating client information.
    """
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            'company_name': 'Company Name',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'client_type': 'Client Type',
            'address1': 'Address Line 1',
            'address2': 'Address Line 2',
            'postal_code': 'Postal Code',
            'city': 'City',
            'country': 'Country',
            'telephone': 'Telephone',
            'mobile': 'Mobile',
            'email': 'Email',
            'salesman': 'Salesman',
            'manager': 'Manager',
        }
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name', 'tabindex': '1'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'tabindex': '2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'tabindex': '3'}),
            'client_type': forms.Select(attrs={'class': 'form-control', 'tabindex': '4'}),
            'address1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1', 'tabindex': '5'}),
            'address2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2', 'tabindex': '6'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code', 'tabindex': '7'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City', 'tabindex': '8'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country', 'tabindex': '8'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+46 123 456 789', 'tabindex': '9'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+46 123 456 789', 'tabindex': '10'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com', 'tabindex': '11'}),
            'salesman': forms.Select(attrs={'class': 'form-control', 'tabindex': '12'}),
            'manager': forms.Select(attrs={'class': 'form-control', 'tabindex': '13'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
