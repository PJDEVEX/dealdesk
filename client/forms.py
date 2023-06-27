from django import forms
from .models import Client, CLIENT_TYPE_CHOICES


class ClientFilterForm(forms.Form):
    """
    Filter form for filtering clients
    """
    client_type = forms.ChoiceField(
        choices=[('', 'All')] + list(CLIENT_TYPE_CHOICES),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    salesman = forms.CharField(
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
            'client_type': forms.Select(attrs={'class': 'form-control'}),
            'salesman': forms.Select(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
