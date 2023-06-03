from django.contrib import admin
from project.models import Project, Category, Brand
from team.models import Sar


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Define the list of fields to be displayed in the change list view
    list_display = (
        'id',
        'name',
        'client',
        'location',
        'brand',
        'category',
        'type_of_construction',
        'project_status',
        'est_closing_date',        
        'est_date_of_delivery',
        'potential_value',
        'winning_chance',
        'forecast_pxp',
        'salesman',
        )
    # Define the list of fields to be used for filtering the change list view
    list_filter = (
        'project_status',
        'type_of_construction',
        'winning_chance',
        'brand',
        'category',
        'salesman',
        )
    # Search fields allow searching by project name, location, brand, category,
    # salesman, or client company name.
    search_fields = [
        'name',
        'location',
        'brand__brand',
        'category__category',
        'salesman__first_name',
        'salesman__last_name',
        'client__company_name',
        ]
    # Add a helper text so that user finds it easy to search
    change_list_template = 'admin/project/project_change_list.html'


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    # Define the list of fields to be displayed in the change list view
    list_display = (
        'id',
        'brand',
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Define the list of fields to be displayed in the change list view
    list_display = (
        'id',
        'category',
        )
