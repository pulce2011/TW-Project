from django import forms
from .models import Valutazione
from shop.models import *

# Possibili condizioni della valutazione

CONDITION_CHOICES = [
        ("excellent", "Eccellente"),
        ("good", "Buono"),
        ("fair", "Discreto"),
        ("damaged", "Danneggiato"),
        ("not_working", "Non funzionante"),
    ]

# Possibili memorie della valutazione

MEMORY_CHOICES = [
    (64, '64 GB'),
    (128, '128 GB'),
    (256, '256 GB'),
    (512, '512 GB'),
    (1024, '1 TB'),
    ]


# Form per la valutazione

class ValutazioneForm(forms.ModelForm):

    memoria = forms.ChoiceField(choices=MEMORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    condizione = forms.ChoiceField(choices=CONDITION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Valutazione
        fields = ['prodotto', 'memoria', 'condizione', 'schermo_rotto', 'back_rotto', 'stato_batteria', 'bloccato', 'commento']
        widgets = {
            'prodotto': forms.Select(attrs={'class': 'form-control'}),
            'schermo_rotto': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'back_rotto': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'stato_batteria': forms.NumberInput(attrs={'class': 'form-control'}),
            'bloccato': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'commento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    # Imposta i prodotti in ordine alfabetico
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prodotto'].queryset = Prodotto.objects.all().order_by('nome')