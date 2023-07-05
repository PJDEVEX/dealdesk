from django.urls import path
from .views import (
    LeadListView,
    LeadCreateView
    )

app_name = 'lead_master'

urlpatterns = [
    path('list/', LeadListView.as_view(), name='lead_list'),
    path("new/", LeadCreateView.as_view(), name='lead_new'),
]
