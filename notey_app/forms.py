from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Note


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="name")
    email = forms.EmailField(label="email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Re-enter Password", widget=forms.PasswordInput)

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


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="name")
    password = forms.CharField(label="password", widget=forms.PasswordInput)