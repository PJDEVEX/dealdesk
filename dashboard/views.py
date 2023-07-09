import json
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.html import json_script
from django.shortcuts import render
from django.views.generic import TemplateView
from lead_master.models import LeadMaster
from django.db import models
from decimal import Decimal


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        # Create a context dictionary to pass data to the template
        context = super().get_context_data(**kwargs)
        
        # Total Leads
        leads_count = LeadMaster.objects.count()
        context['leads_count'] = leads_count
        
        # Average Potential Value
        average_potential_value = LeadMaster.objects.aggregate(models.Avg('potential_value'))['potential_value__avg']
        context['average_potential_value'] = int(average_potential_value) if average_potential_value else 0
        
        # Total Forecasted Potential Value
        total_forecasted_potential_value = LeadMaster.objects.aggregate(models.Sum('forecast_pxp'))['forecast_pxp__sum']
        context['total_forecasted_potential_value'] = int(total_forecasted_potential_value) if total_forecasted_potential_value else 0
        
        # Top Salesperson
        top_salesperson = LeadMaster.objects.values('salesman__first_name').annotate(lead_count=models.Count('id')).order_by('-lead_count').first()
        context['top_salesperson'] = f"{top_salesperson['salesman__first_name']}"

        # Category with Most Leads
        category_with_most_leads = LeadMaster.objects.values('category__category').annotate(lead_count=models.Count('id')).order_by('-lead_count').first()
        context['category_with_most_leads'] = category_with_most_leads['category__category']
        
        # Leads Won
        leads_won_count = LeadMaster.objects.filter(lead_status='Won').count()
        context['leads_won_count'] = leads_won_count

        # Lead Winning Chance Distribution
        winning_chance_distribution = LeadMaster.objects.values('winning_chance').annotate(count=models.Count('id'))
        winning_chance_labels = ['No Chance(0%)', 'Very Low(20%)', 'May be(50%)', 'Highly Likely(75%)', 'WON PENDING PO(90%)', 'WON with PO(100%)']
        winning_chance_data = [0, 0, 0, 0, 0, 0]

        for item in winning_chance_distribution:
            winning_chance = item['winning_chance']
            count = item['count']
            
            if winning_chance == Decimal('0.00'):
                index = 0
            elif winning_chance == Decimal('0.20'):
                index = 1
            elif winning_chance == Decimal('0.50'):
                index = 2
            elif winning_chance == Decimal('0.75'):
                index = 3
            elif winning_chance == Decimal('0.90'):
                index = 4
            elif winning_chance == Decimal('1.00'):
                index = 5
            
            winning_chance_data[index] += count

        context['winning_chance_labels'] = winning_chance_labels
        context['winning_chance_data'] = winning_chance_data

        return context
