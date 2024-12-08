from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

class UserRegistrationForm(UserCreationForm):
    nome = forms.CharField(max_length=20, required=True)
    cognome = forms.CharField(max_length=20, required=True)
    numero_di_telefono = forms.CharField(min_length=10, max_length=10, required=True)
    email = forms.EmailField(max_length=254, required=True, validators=[EmailValidator()])

    class Meta:
        model = User
        fields = ['nome', 'cognome', 'email', 'numero_di_telefono', 'username', 'password1', 'password2',]
