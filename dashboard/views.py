from django.shortcuts import render
from django.views.generic import TemplateView
from lead_master.models import LeadMaster
from django.db import models


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        # Create a context dictionary to pass data to the template
        context = super().get_context_data(**kwargs)
        
        # Total Leads
        leads_count = LeadMaster.objects.count()
        context['leads_count'] = leads_count
        
        # Average Potential Value
        average_potential_value = LeadMaster.objects.aggregate(models.Avg('potential_value'))['potential_value__avg']
        context['average_potential_value'] = average_potential_value
        
        # Total Forecasted Potential Value
        total_forecasted_potential_value = LeadMaster.objects.aggregate(models.Sum('forecast_pxp'))['forecast_pxp__sum']
        context['total_forecasted_potential_value'] = total_forecasted_potential_value
        
        # Top Salesperson
        top_salesperson = LeadMaster.objects.values('salesman__first_name').annotate(lead_count=models.Count('id')).order_by('-lead_count').first()
        context['top_salesperson'] = f"{top_salesperson['salesman__first_name']}"

        
        # Category with Most Leads
        category_with_most_leads = LeadMaster.objects.values('category__category').annotate(lead_count=models.Count('id')).order_by('-lead_count').first()
        context['category_with_most_leads'] = category_with_most_leads['category__category']
        
        # Leads Won
        leads_won_count = LeadMaster.objects.filter(lead_status='Won').count()
        context['leads_won_count'] = leads_won_count
        
        return context
