from django.urls import path
from .views import ClientListView

app_name = 'client'

urlpatterns = [
    path('list/', ClientListView.as_view(), name='client-list'),
]
