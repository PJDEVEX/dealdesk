from django.shortcuts import render
from django.views.generic import TemplateView
from lead_master.models import LeadMaster


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        # Create a context dictionary to pass data to the template
        context = super().get_context_data(**kwargs)
        # Retrieve all leads from the LeadMaster model
        leads = LeadMaster.objects.all()
        context['leads'] = leads
        return context
