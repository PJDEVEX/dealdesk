from django.contrib import admin
from task_manager.models import TaskManager
from team.models import Sar

# Register TaskManager model


@admin.register(TaskManager)
class TaskManagerAdmin(admin.ModelAdmin):
    # Define the list of fields to be displayed in the list view
    list_display = (
        'id',
        'title',
        'due_date',
        'status',
        'priority',
        'assigned_to',
    )
    # Define the list of fields to be used for filtering the change list view
    list_filter = (
        'status',
        'priority',
    )
