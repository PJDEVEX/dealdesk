from django.urls import path
from .views import (ClientListView, ClientCreateView)

app_name = 'client'

urlpatterns = [
    path('list/', ClientListView.as_view(), name='client_list'),
    path("new/", ClientCreateView.as_view(), name="client_new")
]
