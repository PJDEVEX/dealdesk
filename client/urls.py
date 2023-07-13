from django.urls import path
from .views import (
    ClientListView,
    ClientCreateView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
)


app_name = 'client'

urlpatterns = [
    path('list/', ClientListView.as_view(), name='client_list'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
