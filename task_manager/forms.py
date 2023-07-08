from django import forms
from django.forms import DateInput, TimeInput
from django.utils import timezone
from .models import TaskManager, STATUS_CHOICES, PRIORITY_CHOICES
from team.models import Sar


class TaskManagerForm(forms.ModelForm):
    """
    Form for creating and updating task information.
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
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title', 'tabindex': '1'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'tabindex': '2'}),
            'due_date': DateInput(attrs={'class': 'vDateField form-control', 'required': '', 'id': 'id_due_date_0'}),
            'due_time': TimeInput(attrs={'class': 'vTimeField form-control', 'required': '', 'id': 'id_due_date_1'}),
            'status': forms.Select(attrs={'class': 'form-control', 'tabindex': '4'}),
            'priority': forms.Select(attrs={'class': 'form-control', 'tabindex': '5'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control', 'tabindex': '6'}),
        }

    def clean_due_date(self):
        """
        Validate the due date to ensure it is in the future.
        """
        due_date = self.cleaned_data['due_date']
        due_time = self.cleaned_data['due_time']
        due_datetime = timezone.datetime.combine(due_date, due_time)
        if due_datetime < timezone.now():
            raise forms.ValidationError("Due date and time must be in the future.")
        return due_datetime


class TaskManagerFilterForm(forms.Form):
    """
    Filter form for filtering tasks.
    """
    status = forms.ChoiceField(
        choices=[('', 'All')] + STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'tabindex': '1'}),
        required=False
    )
    priority = forms.ChoiceField(
        choices=[('', 'All')] + PRIORITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'tabindex': '2'}),
        required=False
    )
    assigned_to = forms.ModelChoiceField(
        queryset=Sar.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'tabindex': '3'}),
        required=False
    )
    search_keyword = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search tasks', 'tabindex': '4'}),
        required=False
    )
