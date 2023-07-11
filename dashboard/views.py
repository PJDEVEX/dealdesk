from django.shortcuts import render
from django.views.generic import TemplateView
from lead_master.models import LeadMaster, WINNING_CHANCE
from django.db import models
from decimal import Decimal
from django.db.models.functions import TruncMonth
from django.db.models import Sum


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
        winning_chance_labels = [str(chance[1]) for chance in WINNING_CHANCE]
        winning_chance_data = [0] * len(winning_chance_labels)

        for item in winning_chance_distribution:
            winning_chance = item['winning_chance']
            count = item['count']
            
            index = next((i for i, chance in enumerate(WINNING_CHANCE) if chance[0] == winning_chance), None)
            if index is not None:
                winning_chance_data[index] += count

        context['winning_chance_element_id'] = 'lead_winning_chance_chart'
        context['winning_chance_labels'] = winning_chance_labels
        context['winning_chance_data'] = winning_chance_data

        # Sales Forecast
        sales_forecast_data = LeadMaster.objects.annotate(month=TruncMonth('est_closing_date')).values('month').annotate(total_forecast_pxp=Sum('forecast_pxp')).order_by('month')
        sales_forecast_labels = [data['month'].strftime('%B %Y') for data in sales_forecast_data]
        sales_forecast_values = [data['total_forecast_pxp'] for data in sales_forecast_data]

        context['sales_forecast_element_id'] = 'lead_forecast_pxp_chart'
        context['sales_forecast_labels'] = sales_forecast_labels
        context['sales_forecast_values'] = sales_forecast_values

        return context
