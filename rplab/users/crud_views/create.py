from shop.models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Classe per creare brand

class BrandCreateView(CreateView):
    model = Brand
    fields = ['nome', 'immagine']
    template_name = 'users/CRUD/create.html'
    success_url = reverse_lazy('users:gestione')


# Classe per creare prodotto

class ProdottoCreateView(CreateView):
    model = Prodotto
    fields = ['nome', 'descrizione', 'modello', 'immagine']
    template_name = 'users/CRUD/create.html'
    success_url = reverse_lazy('users:gestione')


# Classe per creare dettaglio

class DettaglioCreateView(CreateView):
    model = Dettagli
    fields = ['prodotto', 'condizione', 'prezzo', 'quantita']
    template_name = 'users/CRUD/create.html'
    success_url = reverse_lazy('users:gestione')


# Classe per creare comanda

class ComandaCreateView(CreateView):
    model = Comanda
    fields = ['utente', 'dettagli']
    template_name = 'users/CRUD/create.html'
    success_url = reverse_lazy('users:gestione')