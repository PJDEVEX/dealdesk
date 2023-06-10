from django.shortcuts import render
from django.views import View


class LeadMaster(View):
    def get(self, request):
        # view logic here
        return render(request, 'lead_master/lead_master.html')
