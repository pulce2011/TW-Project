from django import forms
from .models import Valutazione
from shop.models import *


class ValutazioneForm(forms.ModelForm):
    class Meta:
        model = Valutazione
        fields = ['prodotto', 'memoria', 'condizione', 'schermo_rotto', 'back_rotto', 'stato_batteria', 'bloccato', 'commento']
        widgets = {
            'prodotto': forms.Select(attrs={'class': 'form-control'}),
            'memoria': forms.NumberInput(attrs={'class': 'form-control'}),
            'condizione': forms.Select(attrs={'class': 'form-control'}),
            'schermo_rotto': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'back_rotto': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'stato_batteria': forms.NumberInput(attrs={'class': 'form-control'}),
            'bloccato': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'commento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }