from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Note
from django.contrib.auth import get_user
from django.forms.widgets import HiddenInput


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
        fields = ('author', 'create_date', 'category', 'title', 'text')
        # Fields that you should be able to edit while doin notes

        labels = {
            'create_date': 'date',
            'category': 'category',
            'title': 'title',
            'text': 'text',
            }

        widgets = {

            'create_date': forms.DateInput(attrs={'type': 'date'}),
            'category': forms.TextInput(attrs={'class': 'category-note note-field form-field-s'}),
            'title': forms.TextInput(attrs={'class': 'title-note note-field'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea note-text note-field'})
        }

        """
        widgets sets class for css, allows to edit content via class we set here
        """

    def __init__(self, *args, **kwargs):
        # Get the currently logged-in user from the form's kwargs
        user = kwargs.pop('user', None)
        super(NoteForm, self).__init__(*args, **kwargs)

        # Set the 'author' field to the logged-in user
        if user:
            self.fields['author'].initial = user
            self.fields['author'].widget = forms.HiddenInput()



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="name")
    password = forms.CharField(label="password", widget=forms.PasswordInput)



# TODO styling for form, check all notes working

