from django.shortcuts import render, redirect, get_object_or_404
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