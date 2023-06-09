from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Client


class ClientListView(ListView):
    model = Client
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter clients by client_type and salesman
        client_type = self.request.GET.get('client_type')
        salesman = self.request.GET.get('salesman')
        if client_type:
            queryset = queryset.filter(client_type=client_type)
        if salesman:
            queryset = queryset.filter(salesman=salesman)

        # Search clients by company_name and country
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(company_name__icontains=search_query) |
                Q(country__icontains=search_query)
            )

        return queryset