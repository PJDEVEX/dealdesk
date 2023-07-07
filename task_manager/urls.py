from django.urls import path
from .views import TaskListView
from django.urls import include

app_name = 'task_manager'

urlpatterns = [
    path('list/', TaskListView.as_view(), name='task_list'),
]
