from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    )
from .forms import LeadMasterFilterForm, LeadMasterForm
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


class LeadCreateView(CreateView):
    model = LeadMaster
    form_class = LeadMasterForm
    template_name = 'lead_master/lead_create.html'
    success_url = reverse_lazy('lead_master:lead_list')

    def form_invalid(self, form):
        # Add styling to invalid fields
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-invalid'
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class LeadDetailView(DetailView):
    model = LeadMaster
    template_name = 'lead_master/lead_detail.html'
    context_object_name = 'lead'

    def get_object(self, queryset=None):
        """
        Retrieve the object based on the pk parameter.
        Returns a 404 response if the object doesn't exist.
        """
        pk = self.kwargs.get('pk')
        return get_object_or_404(LeadMaster, pk=pk)


class LeadUpdateView(UpdateView):
    model = LeadMaster
    template_name = "lead_master/lead_edit.html"
    form_class = LeadMasterForm

    def get_success_url(self):
        # Get the updated lead instance
        lead = self.get_object()
        # Return the URL for the lead_detail view with the lead's id 
        # as a parameter
        return reverse('lead_master:lead_detail', kwargs={'pk': lead.pk})

    def form_invalid(self, form):
        # Override form_invalid to add styling to invalid fields
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-invalid'
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
