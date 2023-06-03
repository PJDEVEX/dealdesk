from django.contrib import admin
from client.models import Client

# Register the client odel


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # Define the list of fields to be displayed in the change list view
    list_display = (
        'company_name',
        'first_name',
        'salesman',
        'created_on',
        'updated_on'
        )
    # Define the list of fields to be used for filtering the change list view
    list_filter = (
        'client_type',
        'city',
        'country',
        'salesman',
        'manager'
        )
