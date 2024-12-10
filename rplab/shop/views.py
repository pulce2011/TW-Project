from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .forms import *
from .models import *
from .crud_views.create import *
from .crud_views.update import *
from .crud_views.delete import *


#Vista HomeShop

def home(request):
    brands = Brand.objects.all()
    prodotti = Prodotto.objects.all().order_by('-data_pub')[:6] #Visualizza solo gli ultimi 6 prodotti più recenti

    ctx = {"brands":brands,
           "prodotti":prodotti,
           "evidenza":"in evidenza"}

    return render(request, 'shop/home_shop.html', context=ctx)


#ListView prodotti

class AllProductsListView(ListView):
    model = Prodotto
    template_name = "shop/all_prodotti.html"
    context_object_name = "prodotti"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tot"] = self.model.objects.all().count()
        return context
    

#ListView brands

class AllBrandsListView(LoginRequiredMixin, ListView):
    model = Brand
    template_name = "shop/all_brand.html"
    context_object_name = "brands"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tot"] = self.model.objects.all().count()
        return context


#ListView Esplora Brand

class ExploreProdcutsListView(ListView):
    model = Prodotto
    template_name = "shop/esplora_brand.html"
    context_object_name = "prodotti"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nome_brand"] = self.kwargs["nome"]
        return context

    def get_queryset(self):
        arg = self.kwargs["nome"]
        qs = self.model.objects.filter(modello=get_object_or_404(Brand, nome__icontains=arg))
        return qs    


#DetailView Prodotto
    
class ProductDetailView(DetailView):
    model = Prodotto
    template_name = "shop/detail_product.html"
    context_object_name = "prodotto"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["prezzoda"] = Dettagli.objects.get(prodotto=self.object, condizione='used').prezzo
        except:
            context["prezzoda"] = " non disponibile."
        return context
    
    
#Vista pagina acquisto

@login_required
def acquista(request, pk):
    if request.method == "POST":
        form = CondizioneProdottoForm(request.POST)
        if form.is_valid():
            condizione = form.cleaned_data['condizione']
            prodotto = get_object_or_404(Prodotto, pk=pk)
            return redirect('shop:checkout', condizione=condizione, prodotto_pk=prodotto.pk)
    else:
        form = CondizioneProdottoForm()
        return render(request, 'shop/acquista.html', {"form":form})


#Vista pagina checkout

@login_required
def checkout(request, condizione, prodotto_pk):
    prodotto = get_object_or_404(Prodotto, pk=prodotto_pk)
    dettaglio = get_object_or_404(Dettagli, prodotto=prodotto, condizione=condizione)

    if request.method == "POST" and request.user.is_authenticated:
        user = request.user
        return redirect('shop:confermato', utente_pk=user.pk, dettaglio_pk=dettaglio.pk)
    else:
        return render(request, 'shop/checkout.html', {"prodotto":prodotto, "dettaglio":dettaglio})
    

# Vista per la ricerca di prodotti

def search(request):
    search_ctx = request.GET.get('search')
    if search_ctx:
        list_products = Prodotto.objects.filter(nome__icontains=search_ctx)
    else:
        return redirect('shop:homeshop')
    return render(request, 'shop/all_prodotti.html', {'search_ctx': search_ctx, 'prodotti': list_products})


# Vista pagina di acquisto effettuato

@login_required
def acquistoeffettuato(request, utente_pk, dettaglio_pk):
    utente = get_object_or_404(User, pk=utente_pk)
    dettaglio = get_object_or_404(Dettagli, pk=dettaglio_pk)

    if utente and dettaglio:
        new_comanda = Comanda()
        new_comanda.utente = utente
        new_comanda.dettagli = dettaglio
        new_comanda.data_acquisto = timezone.now()
        new_comanda.save()
        dettaglio.quantita -= 1
        dettaglio.save()

    return render(request, 'shop/acquisto_effettuato.html', {'utente':utente, 'dettagli':dettaglio})


# Vista pagina homepage per le operazione CRUD

@staff_member_required
def crud_operations(request):
    operation = request.GET.get('operazione')
    model = request.GET.get('modello')

    if operation and model:
        url_name = f"{model}_{operation}" 
        print("URL_NAME: " + url_name) # Es: "brand_create"
        return redirect('shop:' + url_name)
    else:
        return render(request, "shop/CRUD/home_crud.html")
