from django.contrib import admin
from django.apps import apps  # Import the apps module from Django

# The apps module provides tools for working with Django applications
# It allows access to various application configurations and models


all_models = apps.get_models()

for model in all_models:
    try:
        admin.site.register(model)  # Register the model in the admin site
    except admin.sites.AlreadyRegistered:
        pass  # If the model is already registered, skip it
