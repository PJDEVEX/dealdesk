from django.contrib import admin
from project.models import Project, Category, Brand
# from django.apps import apps  # Import the apps module from Django

# # The apps module provides tools for working with Django applications
# # It allows access to various application configurations and models
# # Here, I register models of all the apps

# all_models = apps.get_models()

# for model in all_models:
#     try:
#         admin.site.register(model)  # Register the model in the admin site
#     except admin.sites.AlreadyRegistered:
#         pass  # If the model is already registered, skip it

# Register the Project, Brand, Category Models in the admin site
admin.site.register(Project)
admin.site.register(Brand)
admin.site.register(Category)
