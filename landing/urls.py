"""
URL configuration for the landing app.
"""
from django.urls import path
from .views import LandingPageView

app_name = 'landing'

urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
    # Other URL patterns specific to the landing app
]
