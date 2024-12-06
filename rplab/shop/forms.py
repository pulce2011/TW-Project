from django import forms


#Form per scegliere condizione prodotto da aquistare

class CondizioneProdottoForm(forms.Form):
    CONDITION_CHOICES = [
        ('new', 'Nuovo'),
        ('used', 'Usato'),
        ('refurbished', 'Ricondizionato'),
    ]
    condizione = forms.ChoiceField(choices=CONDITION_CHOICES, label="Seleziona condizione")
