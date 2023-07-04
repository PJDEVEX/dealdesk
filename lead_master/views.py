from django.shortcuts import render
from django.views.generic import ListView
from .forms import LeadMasterFilterForm
from .models import LeadMaster


class LeadListView(ListView):
    model = LeadMaster
    template_name = 'lead_master/lead_list.html'
    context_object_name = 'leads'
    paginate_by = 10

    def get_queryset(self):
        # Initial queryset of leads
        queryset = super().get_queryset()

        # Get filter parameters
        form = LeadMasterFilterForm(self.request.GET)
        if form.is_valid():
            client = form.cleaned_data['client']
            salesman = form.cleaned_data['salesman']
            type_of_construction = form.cleaned_data['type_of_construction']
            lead_status = form.cleaned_data['lead_status']
            winning_chance = form.cleaned_data['winning_chance']
            brand = form.cleaned_data['brand']
            category = form.cleaned_data['category']
            search_keyword = form.cleaned_data['search_keyword']

        # Apply filters to the queryset if provided
        if client:
            queryset = queryset.filter(client=client)
        if salesman:
            queryset = queryset.filter(salesman=salesman)
        if type_of_construction:
            queryset = queryset.filter(type_of_construction=type_of_construction)
        if lead_status:
            queryset = queryset.filter(lead_status=lead_status)
        if winning_chance:
            queryset = queryset.filter(winning_chance=winning_chance)
        if brand:
            queryset = queryset.filter(brand=brand)
        if category:
            queryset = queryset.filter(category=category)
        if search_keyword:
            queryset = queryset.filter(
                name__icontains=search_keyword
            )

        return queryset

    def get_context_data(self, **kwargs):
        """
        Add context data for rendering the template.
        """
        context = super().get_context_data(**kwargs)
        context['filter_form'] = LeadMasterFilterForm(self.request.GET)
        return context
