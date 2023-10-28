from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Mood, Advice
# registration related
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from django.views import View
from django.contrib import messages

# Create your views here.

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        # Add any additional logic you want here
        return response


def index(request):
    return render(request, 'notey_app/home.html')


class AboutView(TemplateView):
    template_name = 'notey_app/about.html'


class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('index')


class NotesView(LoginRequiredMixin, TemplateView):
    template_name = 'notey_app/notes.html'


class MoodView(LoginRequiredMixin, TemplateView):
    template_name = 'notey_app/mood.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mood_choices'] = Mood.MOOD_CHOICES
        return context


class SaveMoodView(LoginRequiredMixin, View):
    login_url = 'login/'
    redirect_field_name = 'notey_app/moodd_advice.html'  # redirect to detail view

    def post(self, request):
        selected_mood = request.POST.get('mood')

        if selected_mood:
            # Create and save the Mood object with the selected mood
            mood = Mood.objects.create(my_mood=selected_mood)
            messages.success(request, 'Saved')
        else:
            messages.error(request, 'Something went wrong.')

        if request.method == 'POST':
            selected_mood = request.POST.get('mood')
            if selected_mood:
                # Retrieve advice based on the selected mood
                advice = Advice.objects.filter(mood_option=selected_mood).first()

                print("Selected Mood:", selected_mood)
                print("Advice:", advice)

                if selected_mood:
                    # Construct the image filename based on the selected mood
                    mood_image_filename = f"{selected_mood}.PNG"

                    # Retrieve advice based on the selected mood
                    advice = Advice.objects.filter(mood_option=selected_mood).first()


                    return render(request, 'notey_app/mood_advice.html',
                                  {'advice': advice, 'selected_mood': selected_mood,
                                   'mood_image_filename': mood_image_filename})
                return render(request, 'notey_app/mood.html')