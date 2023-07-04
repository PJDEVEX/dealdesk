from django import forms
from .models import LeadMaster, TYPE_OF_CONSTRUCTION, LEAD_STATUS, WINNING_CHANCE
from client.models import Client
from team.models import Sar, Manager
from .models import Brand, Category


class LeadMasterFilterForm(forms.Form):
    """
    Filter form for filtering lead masters
    """
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
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
    type_of_construction = forms.ChoiceField(
        choices=[('', 'All')] + TYPE_OF_CONSTRUCTION,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    lead_status = forms.ChoiceField(
        choices=[('', 'All')] + LEAD_STATUS,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    winning_chance = forms.ChoiceField(
        choices=[('', 'All')] + WINNING_CHANCE,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )


class LeadMasterForm(forms.ModelForm):
    """
    Form for creating and updating lead master information.
    """
    class Meta:
        model = LeadMaster
        fields = '__all__'
        labels = {
            'name': 'Name',
            'client': 'Client',
            'location': 'Location',
            'brand': 'Brand',
            'salesman': 'Salesman',
            'manager': 'Manager',
            'type_of_construction': 'Type of Construction',
            'category': 'Category',
            'lead_status': 'Lead Status',
            'est_closing_date': 'Estimated Closing Date',
            'est_date_of_delivery': 'Estimated Date of Delivery',
            'potential_value': 'Potential Value',
            'winning_chance': 'Winning Chance',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'tabindex': '1'}),
            'client': forms.Select(attrs={'class': 'form-control', 'tabindex': '2'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location', 'tabindex': '3'}),
            'brand': forms.Select(attrs={'class': 'form-control', 'tabindex': '4'}),
            'salesman': forms.Select(attrs={'class': 'form-control', 'tabindex': '5'}),
            'manager': forms.Select(attrs={'class': 'form-control', 'tabindex': '6'}),
            'type_of_construction': forms.Select(attrs={'class': 'form-control', 'tabindex': '7'}),
            'category': forms.Select(attrs={'class': 'form-control', 'tabindex': '8'}),
            'lead_status': forms.Select(attrs={'class': 'form-control', 'tabindex': '9'}),
            'est_closing_date': forms.DateInput(attrs={'class': 'form-control', 'tabindex': '10'}),
            'est_date_of_delivery': forms.DateInput(attrs={'class': 'form-control', 'tabindex': '11'}),
            'potential_value': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Potential Value', 'tabindex': '12'}),
            'winning_chance': forms.Select(attrs={'class': 'form-control', 'tabindex': '13'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.all()
        self.fields['salesman'].queryset = Sar.objects.all()
        self.fields['manager'].queryset = Manager.objects.all()
        self.fields['brand'].queryset = Brand.objects.all()
        self.fields['category'].queryset = Category.objects.all()
