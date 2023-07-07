from django import forms
from django.forms import DateTimeInput
from .models import TaskManager, STATUS_CHOICES, PRIORITY_CHOICES
from team.models import Sar


class TaskManagerFilterForm(forms.Form):
    """
    Filter form for filtering tasks in the Task Manager.
    """
    status = forms.ChoiceField(
        choices=[('', 'All')] + list(STATUS_CHOICES),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    priority = forms.ChoiceField(
        choices=[('', 'All')] + list(PRIORITY_CHOICES),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    assigned_to = forms.ModelChoiceField(
        queryset=Sar.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )


class TaskManagerForm(forms.ModelForm):
    """
    Form for creating and updating tasks in the Task Manager.
    """

    class Meta:
        model = TaskManager
        fields = '__all__'
        labels = {
            'title': 'Title',
            'description': 'Description',
            'due_date': 'Due Date',
            'status': 'Status',
            'priority': 'Priority',
            'assigned_to': 'Assigned To',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'tabindex': '1'}),
    'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description', 'tabindex': '2'}),
    'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime', 'tabindex': '3'}),
    'status': forms.Select(attrs={'class': 'form-control', 'tabindex': '4'}),
    'priority': forms.Select(attrs={'class': 'form-control', 'tabindex': '5'}),
    'assigned_to': forms.Select(attrs={'class': 'form-control', 'tabindex': '6'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = Sar.objects.all()
