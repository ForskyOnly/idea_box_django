from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Idea


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Nom utilisateur")
    email = forms.EmailField()
    password1 = forms.CharField(label="Mot de passe*", widget=forms.PasswordInput, help_text="")
    password2 = forms.CharField(label="Confirmer ", widget=forms.PasswordInput, help_text="")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ("titre", "description")