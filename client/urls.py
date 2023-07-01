from django.urls import path
from .views import ClientListView, ClientCreateView, ClientUpdateView

app_name = 'client'

urlpatterns = [
    path('list/', ClientListView.as_view(), name='client_list'),
    path("new/", ClientCreateView.as_view(), name='client_new'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
]
