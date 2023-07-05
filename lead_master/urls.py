from django.urls import path
from .views import (
    LeadListView,
    LeadCreateView,
    LeadDetailView,
    LeadUpdateView,
    )

app_name = 'lead_master'

urlpatterns = [
    path('list/', LeadListView.as_view(), name='lead_list'),
    path("new/", LeadCreateView.as_view(), name='lead_new'),
    path('detail/<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('edit/<int:pk>/', LeadUpdateView.as_view(), name='lead_edit'),
]
