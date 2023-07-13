"""
URL configuration for dealdesk-crm project.
"""
from django.contrib import admin
from django.urls import path, include
from dashboard.views import DashboardView
from landing.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs for the apps
    path('', include('landing.urls', namespace='landing')),
    path('dashboard/', include('dashboard.urls')),
    path('lead_master/', include('lead_master.urls', namespace='lead_master')),
    path('client/', include('client.urls', namespace='client')),
    path(
        'task_manager/',
        include(
            'task_manager.urls',
            namespace='task_manager')),

    # Authentication URLs from allauth
    path('accounts/', include('allauth.urls')),
]
