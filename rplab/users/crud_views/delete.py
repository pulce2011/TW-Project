from django.views.generic import DeleteView
from users.forms import *
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required


# Vista per selezionare il brand da eliminare
@staff_member_required
def select_brand_to_delete(request):
    if request.method == 'POST':
        form = BrandSelectionForm(request.POST)
        if form.is_valid():
            selected_brand = form.cleaned_data['selection']
            return redirect('users:selected_brand_delete', pk=selected_brand.pk)
    else:
        form = BrandSelectionForm()

    return render(request, 'users/CRUD/select_model_to_operate.html', {'form': form})


# Vista per selezionare il prodotto da eliminare
@staff_member_required
def select_prodotto_to_delete(request):
    if request.method == 'POST':
        form = ProdottoSelectionForm(request.POST)
        if form.is_valid():
            selected_prodotto = form.cleaned_data['selection']
            return redirect('users:selected_prodotto_delete', pk=selected_prodotto.pk)
    else:
        form = ProdottoSelectionForm()

    return render(request, 'users/CRUD/select_model_to_operate.html', {'form': form})


# Vista per selezionare il dettaglio da eliminare
@staff_member_required
def select_dettaglio_to_delete(request):
    if request.method == 'POST':
        form = DettaglioSelectionForm(request.POST)
        if form.is_valid():
            selected_dettaglio = form.cleaned_data['selection']
            return redirect('users:selected_dettaglio_delete', pk=selected_dettaglio.pk)
    else:
        form = DettaglioSelectionForm()

    return render(request, 'users/CRUD/select_model_to_operate.html', {'form': form})


# Vista per selezionare la comanda da eliminare
@staff_member_required
def select_comanda_to_delete(request):
    if request.method == 'POST':
        form = ComandaSelectionForm(request.POST)
        if form.is_valid():
            selected_comanda = form.cleaned_data['selection']
            return redirect('users:selected_comanda_delete', pk=selected_comanda.pk)
    else:
        form = ComandaSelectionForm()

    return render(request, 'users/CRUD/select_model_to_operate.html', {'form': form})


# Vista per selezionare la valutazione da eliminare
@staff_member_required
def select_valutazione_to_delete(request):
    if request.method == 'POST':
        form = ValutazioneSelectionForm(request.POST)
        if form.is_valid():
            selected_valutazione = form.cleaned_data['selection']
            return redirect('users:selected_valutazione_delete', pk=selected_valutazione.pk)
    else:
        form = ValutazioneSelectionForm()

    return render(request, 'users/CRUD/select_model_to_operate.html', {'form': form})


# Classe per eliminare brand

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = "users/CRUD/delete.html"
    context_object_name = 'model'
    success_url = reverse_lazy('users:gestione')


# Classe per eliminare prodotto

class ProdottoDeleteView(DeleteView):
    model = Prodotto
    template_name = "users/CRUD/delete.html"
    context_object_name = 'model'
    success_url = reverse_lazy('users:dashboard')


# Classe per eliminare dettaglio

class DettaglioDeleteView(DeleteView):
    model = Dettagli
    template_name = "users/CRUD/delete.html"
    context_object_name = 'model'
    success_url = reverse_lazy('users:dashboard')


# Classe per eliminare comanda

class ComandaDeleteView(DeleteView):
    model = Comanda
    template_name = "users/CRUD/delete.html"
    context_object_name = 'model'
    success_url = reverse_lazy('users:dashboard')

# Classe per eliminare valutazione

class ValutazioneDeleteView(DeleteView):
    model = Valutazione
    template_name = "users/CRUD/delete.html"
    context_object_name = 'model'
    success_url = reverse_lazy('users:dashboard')
