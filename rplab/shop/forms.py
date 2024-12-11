from django import forms
from .models import *


#Form per scegliere condizione prodotto da aquistare

class CondizioneProdottoForm(forms.Form):
    CONDITION_CHOICES = [
        ('new', 'Nuovo'),
        ('used', 'Usato'),
        ('refurbished', 'Ricondizionato'),
    ]
    MEMORY_CHOICES = [
        (64, '64 GB'),
        (128, '128 GB'),
        (256, '256 GB'),
        (512, '512 GB'),
        (1024, '1 TB'),
    ]
    condizione = forms.ChoiceField(choices=CONDITION_CHOICES, label="Seleziona condizione")
    memoria = forms.ChoiceField(choices=MEMORY_CHOICES, label="Seleziona memoria")


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
