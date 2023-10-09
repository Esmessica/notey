from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

# registration related
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login


# Create your views here.
class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return response

def index(request):
    return render(request, 'notey_app/home.html')

class AboutView(TemplateView):
    template_name = 'notey_app/about.html'

