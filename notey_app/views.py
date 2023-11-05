from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
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
# TODO make mood stored for day, if that day mood was selected, load advices instead
# TODO make image show at create form

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # Check if the user has any notes
        user_notes = Note.objects.filter(author=user)
        context['user_has_notes'] = user_notes.exists()
        return context

    def get_queryset(self):
        # Filter notes by the currently logged-in user
        return Note.objects.filter(author=self.request.user).order_by('-create_date')

    """
    with get query set - set SQL query in model. 
    Grab post model.all objects and filter them based on condition.
    """


class CreateNoteView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    redirect_field_name = 'notey_app/note_detail.html'
    form_class = NoteForm
    model = Note

    def form_valid(self, form):
        # Set the author to the currently logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the detail view of the newly created note
        return reverse('notey_app:note_detail', kwargs={'pk': self.object.pk})


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login/'
    redirect_field_name = 'notey_app/note_detail.html'         # redirect to detail view
    form_class = NoteForm
    # mixin require those above
    model = Note

    def form_valid(self, form):
        # Retrieve the existing note by its primary key
        note = Note.objects.get(pk=self.kwargs['pk'])
        # Update the fields based on the submitted form data
        note.title = form.cleaned_data['title']
        note.text = form.cleaned_data['text']
        # Save the updated note
        note.save()
        return redirect('notey_app:note_detail', pk=note.pk)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notey_app:all_notes')


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notey_app/note_detail.html'

    def get_queryset(self):
        # Filter notes by the currently logged-in user
        return Note.objects.filter(author=self.request.user)


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.request.user

    return context