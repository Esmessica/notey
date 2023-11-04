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


# TODO make author for notes field that uses User model
class NoteForm(forms.ModelForm):

    class Meta():
        model = Note
        fields = ('category', 'title', 'text')
        # Fields that you should be able to edit while doin notes

        widgets = {
                'category': forms.TextInput(attrs={'class': 'category-note note-field form-field-s'}),
                'title': forms.TextInput(attrs={'class': 'title-note note-field'}),
                'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea note-text note-field'})
        }

        """
        widgets sets class for css, allows to edit content via class we set here
        """


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="name")
    password = forms.CharField(label="password", widget=forms.PasswordInput)


# TODO secure notes for user only
# TODO styling for form, check all notes working
# TODO save not working on add notes
