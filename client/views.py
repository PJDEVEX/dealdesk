from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView)
from django.db import IntegrityError, transaction
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
        Add context data for rendering the template.
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


class ClientCreateView(CreateView):
    model = Client
    template_name = "client/client_create.html"
    form_class = ClientForm
    success_url = reverse_lazy('client:client_list')

    def form_invalid(self, form):
        # Override form_invalid to add styling to invalid fields
        for field in form.errors:
            form[field].field.widget.attrs['class'] += 'is-invalid'
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    template_name = "client/client_edit.html"
    form_class = ClientForm

    def get_success_url(self):
        # Get the updated client instance
        client = self.get_object()
        # Return the URL for the client_detail view with the client's id 
        # as a parameter
        return reverse('client:client_detail', kwargs={'pk': client.pk})

    def form_invalid(self, form):
        # Override form_invalid to add styling to invalid fields
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-invalid'
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'
    context_object_name = 'client'

    def get_object(self, queryset=None):
        """
        Retrieve the object based on the pk parameter.
        Returns a 404 response if the object doesn't exist.
        """
        pk = self.kwargs.get('pk')
        return get_object_or_404(Client, pk=pk)


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/client_delete.html'
    success_url = reverse_lazy('client:client_list')
