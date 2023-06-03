from django.contrib import admin
from team.models import Manager, Sar


# Register manager and Sar models
# Register the Project, Brand, Category Models in the admin site
models_to_register = [Sar, Manager]

for model in models_to_register:
    admin.site.register(model)
