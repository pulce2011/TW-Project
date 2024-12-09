from django.views.generic import UpdateView
from shop.forms import *
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


# Vista per selezionare il brand da modificare

def select_brand_to_update(request):
    if request.method == 'POST':
        form = BrandSelectionForm(request.POST)
        if form.is_valid():
            selected_brand = form.cleaned_data['selection']
            return redirect('shop:selected_brand_update', pk=selected_brand.pk)
    else:
        form = BrandSelectionForm()

    return render(request, 'shop/CRUD/select_model_to_operate.html', {'form': form})


# Vista per selezionare il prodotto da modificare

def select_prodotto_to_update(request):
    if request.method == 'POST':
        form = ProdottoSelectionForm(request.POST)
        if form.is_valid():
            selected_prodotto = form.cleaned_data['selection']
            return redirect('shop:selected_prodotto_update', pk=selected_prodotto.pk)
    else:
        form = ProdottoSelectionForm()

    return render(request, 'shop/CRUD/select_model_to_operate.html', {'form': form})


# Vista per selezionare il dettaglio da modificare

def select_dettaglio_to_update(request):
    if request.method == 'POST':
        form = DettaglioSelectionForm(request.POST)
        if form.is_valid():
            selected_dettaglio = form.cleaned_data['selection']
            return redirect('shop:selected_dettaglio_update', pk=selected_dettaglio.pk)
    else:
        form = DettaglioSelectionForm()

    return render(request, 'shop/CRUD/select_model_to_operate.html', {'form': form})


# Vista per selezionare la comanda da modificare

def select_comanda_to_update(request):
    if request.method == 'POST':
        form = ComandaSelectionForm(request.POST)
        if form.is_valid():
            selected_comanda = form.cleaned_data['selection']
            return redirect('shop:selected_comanda_update', pk=selected_comanda.pk)
    else:
        form = ComandaSelectionForm()

    return render(request, 'shop/CRUD/select_model_to_operate.html', {'form': form})



class BrandUpdateView(UpdateView):
    model = Brand
    fields = ['nome', 'immagine']  # I campi che vuoi permettere di modificare
    template_name = 'shop/CRUD/update.html'
    context_object_name = 'model'
    success_url = reverse_lazy('shop:gestione')  # Dove reindirizzare dopo il salvataggio

class ProdottoUpdateView(UpdateView):
    model = Prodotto
    fields = ['nome', 'descrizione', 'modello', 'immagine']  # I campi che vuoi permettere di modificare
    template_name = 'shop/CRUD/update.html'
    context_object_name = 'model'
    success_url = reverse_lazy('shop:gestione')  # Dove reindirizzare dopo il salvataggio

class DettaglioUpdateView(UpdateView):
    model = Dettagli
    fields = ['prodotto', 'condizione', 'prezzo', 'quantita']  # I campi che vuoi permettere di modificare
    template_name = 'shop/CRUD/update.html'
    context_object_name = 'model'
    success_url = reverse_lazy('shop:gestione')  # Dove reindirizzare dopo il salvataggio

class ComandaUpdateView(UpdateView):
    model = Comanda
    fields = ['utente', 'dettagli']  # I campi che vuoi permettere di modificare
    template_name = 'shop/CRUD/update.html'
    context_object_name = 'model'
    success_url = reverse_lazy('shop:gestione')  # Dove reindirizzare dopo il salvataggio
