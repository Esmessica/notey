from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Note


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NoteForm(forms.ModelForm):

    class Meta():
        model = Note
        fields = ('category', 'title', 'text')
        # Fields that you should be able to edit while doin notes

        widgets = {
                'category': forms.TextInput(attrs={'class': 'category-note'}),
                'title': forms.TextInput(attrs={'class': 'title-note'}),
                'text': forms.Textarea(attrs={'class': ' text-content'})
        }

        """
        widgets sets class for css, allows to edit content via class we set here
        """