from django.views.generic import UpdateView
from users.forms import *
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required


# Vista per selezionare il brand da modificare
@staff_member_required
def select_brand_to_update(request):
    if request.method == 'POST':
        form = BrandSelectionForm(request.POST)
        if form.is_valid():
            selected_brand = form.cleaned_data['selection']
            return redirect('users:selected_brand_update', pk=selected_brand.pk)
    else:
        form = BrandSelectionForm()

    return render(request, 'users/CRUD/select_model_to_operate.html', {'form': form})


# Vista per selezionare il prodotto da modificare
@staff_member_required
def select_prodotto_to_update(request):
    if request.method == 'POST':
        form = ProdottoSelectionForm(request.POST)
        if form.is_valid():
            selected_prodotto = form.cleaned_data['selection']
            return redirect('users:selected_prodotto_update', pk=selected_prodotto.pk)
    else:
        form = ProdottoSelectionForm()

    return render(request, 'users/CRUD/select_model_to_operate.html', {'form': form})


# Vista per selezionare il dettaglio da modificare
@staff_member_required
def select_dettaglio_to_update(request):
    if request.method == 'POST':
        form = DettaglioSelectionForm(request.POST)
        if form.is_valid():
            selected_dettaglio = form.cleaned_data['selection']
            return redirect('users:selected_dettaglio_update', pk=selected_dettaglio.pk)
    else:
        form = DettaglioSelectionForm()

    return render(request, 'users/CRUD/select_model_to_operate.html', {'form': form})


# Vista per selezionare la comanda da modificare
@staff_member_required
def select_comanda_to_update(request):
    if request.method == 'POST':
        form = ComandaSelectionForm(request.POST)
        if form.is_valid():
            selected_comanda = form.cleaned_data['selection']
            return redirect('users:selected_comanda_update', pk=selected_comanda.pk)
    else:
        form = ComandaSelectionForm()

    return render(request, 'users/CRUD/select_model_to_operate.html', {'form': form})


# Vista per selezionare la valutazione da modificare
@staff_member_required
def select_valutazione_to_update(request):
    if request.method == 'POST':
        form = ValutazioneSelectionForm(request.POST)
        if form.is_valid():
            selected_valutazione = form.cleaned_data['selection']
            return redirect('users:selected_comanda_update', pk=selected_valutazione.pk)
    else:
        form = ValutazioneSelectionForm()

    return render(request, 'users/CRUD/select_model_to_operate.html', {'form': form})


# Classe per agggiornare brand

class BrandUpdateView(UpdateView):
    model = Brand
    fields = ['nome', 'immagine']
    template_name = 'users/CRUD/update.html'
    context_object_name = 'model'
    success_url = reverse_lazy('users:gestione')


# Classe per agggiornare prodotto

class ProdottoUpdateView(UpdateView):
    model = Prodotto
    fields = ['nome', 'descrizione', 'modello', 'immagine']
    template_name = 'users/CRUD/update.html'
    context_object_name = 'model'
    success_url = reverse_lazy('users:gestiodashboardne')


# Classe per agggiornare dettaglio

class DettaglioUpdateView(UpdateView):
    model = Dettagli
    fields = ['prodotto', 'condizione', 'prezzo', 'quantita']
    template_name = 'users/CRUD/update.html'
    context_object_name = 'model'
    success_url = reverse_lazy('users:dashboard')


# Classe per agggiornare comanda

class ComandaUpdateView(UpdateView):
    model = Comanda
    fields = ['utente', 'dettagli', 'completata']
    template_name = 'users/CRUD/update.html'
    context_object_name = 'model'
    success_url = reverse_lazy('users:dashboard')

# Classe per agggiornare valutazione

class ValutazioneUpdateView(UpdateView):
    model = Valutazione
    fields = ['utente', 'prodotto', 'memoria', 'condizione', 'schermo_rotto', 'back_rotto', 'stato_batteria', 'bloccato', 'commento', 'valore', 'completata']
    template_name = 'users/CRUD/update.html'
    context_object_name = 'model'
    success_url = reverse_lazy('users:dashboard')