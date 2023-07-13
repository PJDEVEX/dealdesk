from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

app_name = 'task_manager'

urlpatterns = [
    path('list/', TaskListView.as_view(), name='task_list'),
    path('new/', TaskCreateView.as_view(), name='task_new'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='task_edit'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]
