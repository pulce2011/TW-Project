from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from .forms import *
from .models import *

def home(request):
    return render(request, "sell/home_sell.html")


def valutazione(request):
    if request.method == 'POST':
        form = ValutazioneForm(request.POST)
        if form.is_valid():
            valutazione = form.save(commit=False)
            valutazione.utente = request.user


            # Valutazione prezzo
            prezzo = get_object_or_404(Dettagli, prodotto=valutazione.prodotto, condizione="new", memoria=valutazione.memoria).prezzo * Decimal(0.9)

            if(valutazione.condizione == 'excellent'): #Se condizione == eccellente, prezzo uguale
                pass
            elif(valutazione.condizione == 'good'): #Se condizione == buono, prezzo -10%
                prezzo *= Decimal(0.9)
            elif(valutazione.condizione == 'fair'): #Se condizione == discreto, prezzo -20%
                prezzo *= Decimal(0.8)
            elif(valutazione.condizione == 'damaged'): #Se condizione == danneggiato, -35%
                prezzo *= Decimal(0.65)
            elif(valutazione.condizione == 'not_working'): #Se condizione == non funzionante, -65 %
                prezzo *= Decimal(0.45)
            
            if(valutazione.schermo_rotto): #Se schermo è rotto, prezzo -50%
                prezzo *= Decimal(0.5)
            
            if(valutazione.back_rotto): #Se back è rotto, prezzo - 0%
                prezzo *= Decimal(0.7)

            if(valutazione.stato_batteria >= 95 and valutazione.stato_batteria <= 100): #Se stato batteria compreso tra 95 e 100, prezzo uguale
                pass
            elif(valutazione.stato_batteria >= 90 and valutazione.stato_batteria < 95): #Se stato batteria compreso tra 90 e 94, prezzo -10%
                prezzo *= Decimal(0.9)
            elif(valutazione.stato_batteria >= 80 and valutazione.stato_batteria < 90): #Se stato batteria compreso tra 80 e 89, prezzo -15%
                prezzo *= Decimal(0.85)
            else: #Se stato batteria compreso minore di 79, prezzo -25%
                prezzo *= Decimal(0.75)

            if(valutazione.bloccato):
                prezzo *= Decimal(0.25) #Se bloccato da casa produttrice, prezzo -75%

            valutazione.valore = prezzo

            valutazione.save()
            return redirect('sell:success')  # Reindirizza dopo il salvataggio
    else:
        form = ValutazioneForm()

    context = {
        'prodotti': Prodotto.objects.all(),
        'form': form,
    }
    return render(request, 'sell/valutazione.html', context)

def success(request):
    return render(request, 'sell/success.html')