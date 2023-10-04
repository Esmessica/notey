from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return render(request, 'notey_app/home.html')

class AboutView(TemplateView):
    template_name = 'notey_app/about.html'
