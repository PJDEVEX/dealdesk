from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import TaskManager
from .forms import TaskManagerFilterForm, TaskManagerForm


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


class TaskCreateView(CreateView):
    model = TaskManager
    form_class = TaskManagerForm
    template_name = 'task_manager/task_create.html'
    success_url = reverse_lazy('task_manager:task_list')

    def form_invalid(self, form):
        # Add styling to invalid fields
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-invalid'
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        return super().form_valid(form)