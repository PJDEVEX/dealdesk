from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    """
    View class for rendering the landing page.
    """
    template_name = 'landing/index.html'
