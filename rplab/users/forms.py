from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from shop.models import *
from sell.models import *


# Form per la registrazione utente

class UserRegistrationForm(UserCreationForm):
    numero_di_telefono = forms.CharField(min_length=10, max_length=10, required=True)
    email = forms.EmailField(max_length=254, required=True, validators=[EmailValidator()])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'numero_di_telefono', 'username', 'password1', 'password2',]


# Form per la selezione del Brand 

class BrandSelectionForm(forms.Form):
    selection = forms.ModelChoiceField(queryset=Brand.objects.all(), empty_label="Seleziona un Brand", widget=forms.Select)


# Form per la selezione del Prodotto

class ProdottoSelectionForm(forms.Form):
    selection = forms.ModelChoiceField(queryset=Prodotto.objects.all(), empty_label="Seleziona un Prodotto", widget=forms.Select)


# Form per la selezione del Dettaglio 

class DettaglioSelectionForm(forms.Form):
    selection = forms.ModelChoiceField(queryset=Dettagli.objects.all(), empty_label="Seleziona un Dettaglio", widget=forms.Select)


# Form per la selezione della Comanda 

class ComandaSelectionForm(forms.Form):
    selection = forms.ModelChoiceField(queryset=Comanda.objects.all(), empty_label="Seleziona una Comanda", widget=forms.Select)


# Form per la selezione della Valutazione 

class ValutazioneSelectionForm(forms.Form):
    selection = forms.ModelChoiceField(queryset=Valutazione.objects.all(), empty_label="Seleziona una Comanda", widget=forms.Select)
