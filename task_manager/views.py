from django.views.generic import ListView
from .models import TaskManager
from .forms import TaskManagerFilterForm


class TaskListView(ListView):
    model = TaskManager
    template_name = 'task_manager/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        # Initial queryset of tasks
        queryset = super().get_queryset()

        # Get filter parameters
        form = TaskManagerFilterForm(self.request.GET)
        if form.is_valid():
            status = form.cleaned_data['status']
            priority = form.cleaned_data['priority']
            assigned_to = form.cleaned_data['assigned_to']

        # Apply filters to the queryset if provided
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
        if assigned_to:
            queryset = queryset.filter(assigned_to=assigned_to)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Add context data for rendering the template.
        """
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TaskManagerFilterForm(self.request.GET)
        return context
