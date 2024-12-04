from django.shortcuts import render
from .models import *

def home(request):
    brands = Brand.objects.all()
    prodotti = Prodotto.objects.all().order_by('-data_pub')[:6]

    print(prodotti)

    ctx = {"brands":brands,
           "prodotti":prodotti}

    return render(request, 'shop/homeshop.html', context=ctx)