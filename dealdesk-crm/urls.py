from django.contrib import admin
from django.urls import path, include
from project.views import project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
]
