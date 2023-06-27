from django.contrib import admin
from django.urls import path, include, reverse_lazy
from lead_master.views import LeadMaster

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs for the apps in your project
    path('', include('lead_master.urls')),
    path('client/', include('client.urls')),

    # Authentication URLs from allauth
    path('accounts/', include('allauth.urls')),
]
