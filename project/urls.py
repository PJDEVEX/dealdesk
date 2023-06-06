# urls.py

from django.urls import path
from .import views

urlpatterns = [
    # other URL patterns
    path('', views.project, name='project'),
]
