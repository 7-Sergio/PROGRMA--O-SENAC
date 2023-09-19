from django.urls import path
from . views import list_jobs,details_jobs
from django.views.generic.base import RedirectView


app_name = "jobs"


urlpatterns = [
    path('', list_jobs, name="list"),
    path('<int:pk>/', details_jobs, name='details')
    
]



def list_jobs(request):
    return path('',RedirectView.as_view(url='jobs/'))