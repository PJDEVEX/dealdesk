# urls.py

from django.urls import path
from lead_master.views import LeadMaster

urlpatterns = [
    # other URL patterns
    path('', LeadMaster.as_view(), name='lead_masters'),
]
