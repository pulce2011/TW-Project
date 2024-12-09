from shop.models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView


class BrandCreateView(CreateView):
    model = Brand
    fields = ['nome', 'immagine']
    template_name = 'shop/CRUD/create.html'
    success_url = reverse_lazy('shop:gestione')


class ProdottoCreateView(CreateView):
    model = Prodotto
    fields = ['nome', 'descrizione', 'modello', 'immagine']
    template_name = 'shop/CRUD/create.html'
    success_url = reverse_lazy('shop:gestione')


class DettaglioCreateView(CreateView):
    model = Dettagli
    fields = ['prodotto', 'condizione', 'prezzo', 'quantita']
    template_name = 'shop/CRUD/create.html'
    success_url = reverse_lazy('shop:gestione')

class ComandaCreateView(CreateView):
    model = Comanda
    fields = ['utente', 'dettagli']
    template_name = 'shop/CRUD/create.html'
    success_url = reverse_lazy('shop:gestione')