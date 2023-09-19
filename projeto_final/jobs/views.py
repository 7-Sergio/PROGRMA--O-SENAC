from django.shortcuts import render
from django.views.generic.base import RedirectView

def list_jobs(request):
    return path('',RedirectView.as_view(url='jobs/'))