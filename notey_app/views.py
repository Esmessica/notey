from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Mood, Advice, Note
from .forms import RegisterForm, CustomLoginForm, NoteForm
from django.utils import timezone
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
    authentication_form = CustomLoginForm
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
    redirect_field_name = 'notey_app/mood_advice.html'  # redirect to detail view

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

                # Construct the image filename based on the selected mood
                mood_image_filename = f"{selected_mood}.PNG"

                # Retrieve advice based on the selected mood
                advice = Advice.objects.filter(mood_option=selected_mood).first()

                return render(request, 'notey_app/mood_advice.html',

                              {'advice': advice, 'selected_mood': selected_mood,
                               'mood_image_filename': mood_image_filename})

            return render(request, 'notey_app/mood.html')


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/registration.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/registration.html', {'form': form})


class NoteListView(LoginRequiredMixin, ListView):
    login_url = 'login/'
    redirect_field_name = 'notey_app/note_detail.html'  # redirect to detail view
    model = Note

    def get_queryset(self):
        return Note.objects.order_by('-create_date')

    """

    with get query set - set SQL query in model. 
    Grab post model.all objects and filter them based on condition.
    --lte=less than or equal to current time and order them based by curent date (the dash means DESC order

    """


class CreateNoteView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    redirect_field_name = 'notey_app/note_detail.html'           # redirect to detail view
    form_class = NoteForm
    # mixin require those above
    model = Note


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login/'
    redirect_field_name = 'notey_app/note_detail.html'         # redirect to detail view
    form_class = NoteForm
    # mixin require those above
    model = Note


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('all_notes')


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notey_app/note_detail.html'


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.request.user

    return context