from django import forms
from .models import *


#Form per scegliere condizione prodotto da aquistare

class CondizioneProdottoForm(forms.Form):
    CONDITION_CHOICES = [
        ('new', 'Nuovo'),
        ('used', 'Usato'),
        ('refurbished', 'Ricondizionato'),
    ]
    condizione = forms.ChoiceField(choices=CONDITION_CHOICES, label="Seleziona condizione")

# Form per la selezione del Brand da aggiornare 
class BrandSelectionForm(forms.Form):
    selection = forms.ModelChoiceField(queryset=Brand.objects.all(), empty_label="Seleziona un Brand", widget=forms.Select)

# Form per la selezione del Prodotto da aggiornare 
class ProdottoSelectionForm(forms.Form):
    selection = forms.ModelChoiceField(queryset=Prodotto.objects.all(), empty_label="Seleziona un Prodotto", widget=forms.Select)

# Form per la selezione del Dettaglio da aggiornare 
class DettaglioSelectionForm(forms.Form):
    selection = forms.ModelChoiceField(queryset=Dettagli.objects.all(), empty_label="Seleziona un Dettaglio", widget=forms.Select)

# Form per la selezione della Comanda da aggiornare 
class ComandaSelectionForm(forms.Form):
    selection = forms.ModelChoiceField(queryset=Comanda.objects.all(), empty_label="Seleziona una Comanda", widget=forms.Select)
