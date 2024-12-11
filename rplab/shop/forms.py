from django import forms
from .models import *


#Form per scegliere la condizione del prodotto da aquistare

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
