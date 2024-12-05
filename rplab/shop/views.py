from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Sum
from .forms import *
from .models import *

def home(request):
    brands = Brand.objects.all()
    prodotti = Prodotto.objects.all().order_by('-data_pub')[:6]

    print(prodotti)

    ctx = {"brands":brands,
           "prodotti":prodotti}

    return render(request, 'shop/home_shop.html', context=ctx)

class AllProdcutsListView(ListView):
    model = Prodotto
    template_name = "shop/all_prodotti.html"
    context_object_name = "prodotti"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tot"] = self.model.objects.all().count()
        return context
    


class AllBrandsListView(ListView):
    model = Brand
    template_name = "shop/all_brand.html"
    context_object_name = "brands"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tot"] = self.model.objects.all().count()
        return context
    
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
    
def acquista(request, pk):
    print("LOG: " + str(pk))
    if request.method == "POST":
        form = CondizioneProdottoForm(request.POST)
        if form.is_valid():
            condizione = form.cleaned_data['condizione']
            prodotto = get_object_or_404(Prodotto, pk=pk)
            return redirect('shop:checkout', condizione=condizione, prodotto_pk=prodotto.pk)
    else:
        form = CondizioneProdottoForm()
        return render(request, 'shop/acquista.html', {"form":form})
    
def checkout(request, condizione, prodotto_pk):
    prodotto = get_object_or_404(Prodotto, pk=prodotto_pk)
    dettaglio = get_object_or_404(Dettagli, prodotto=prodotto, condizione=condizione)

    return render(request, 'shop/checkout.html', {"prodotto":prodotto, "dettaglio":dettaglio})
