from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView
from .models import Client
from .forms import ClientForm, ClientFilterForm


class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'clients'
    paginate_by = 10

    def get_queryset(self):
        # Initial queryset of clients
        queryset = super().get_queryset()
        # Get filter parameters
        client_type = self.request.GET.get('client_type')
        salesman = self.request.GET.get('salesman')
        search_keyword = self.request.GET.get('search_keyword')

        # Apply filters to the queryset if provided
        if client_type:
            queryset = queryset.filter(client_type=client_type)

        if salesman:
            queryset = queryset.filter(salesman=salesman)

        if search_keyword:
            queryset = queryset.filter(
                Q(company_name__icontains=search_keyword) |
                Q(first_name__icontains=search_keyword) |
                Q(last_name__icontains=search_keyword) |
                Q(city__icontains=search_keyword) |
                Q(country__icontains=search_keyword)
            )

        return queryset

    def get_context_data(self, **kwargs):
        """
        context data for rendering the template
        """
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ClientFilterForm(self.request.GET)
        context['client_form'] = ClientForm()
        return context

    def post(self, request, *args, **kwargs):
        # Handle form submission via POST request
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client_form.save()
            return redirect('client:client_list')
        else:
            # Handle invalid form submission
            filter_form = ClientFilterForm(request.GET)
            return render(request, self.template_name, {
                'clients': self.get_queryset(),
                'filter_form': filter_form,
                'client_form': client_form,
            })
