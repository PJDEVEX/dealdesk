from django.contrib import admin
from django.urls import path, include

from dashboard.views import DashboardView
from lead_master.views import LeadMaster
from client.views import Client
from task_manager.views import TaskManager

# lead_master/urls.py
app_name = 'lead_master'

# client/urls.py
app_name = 'client'

# task_manager/urls.py
app_name = 'task_manager'


urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs for the apps
    path('', include('dashboard.urls'), name='dashboard'),
    path('lead_master/', include('lead_master.urls', namespace='lead_master'), name='lead_master'),
    path('client/', include('client.urls', namespace='client'), name='client'),
    path('task_manager/', include('task_manager.urls', namespace='task_manager'), name='task_manager'),


    # Authentication URLs from allauth
    path('accounts/', include('allauth.urls')),
]

