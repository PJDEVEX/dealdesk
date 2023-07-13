from django.contrib import admin
from team.models import Sar, Manager


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    # Define the list of fields to be displayed in the list view
    list_display = (
        'id',
        'first_name',
        'last_name',
        'mobile',
        'email',
        'created_on',
        'updated_on',
    )


@admin.register(Sar)
class SarAdmin(admin.ModelAdmin):
    # Define the list of fields to be displayed in the admin view
    list_display = (
        'id',
        'first_name',
        'last_name',
        'mobile',
        'email',
        'manager',
        'created_on',
        'updated_on',
    )
    # Let the user to filer the Sar by manager
    list_filter = (
        ('manager', admin.RelatedOnlyFieldListFilter),
    )
