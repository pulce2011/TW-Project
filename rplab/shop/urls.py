from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='homeshop'), #HomeShop
    path('prodotti/', views.AllProductsListView.as_view(), name="prodotti"), #Lista prodotti
    path('brands/', views.AllBrandsListView.as_view(), name="brands"), #Lista brands
    path('prodotto/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'), #Prodotto nel dettaglio
    path('brand/<str:nome>/', views.ExploreProdcutsListView.as_view(), name="explore_brand"), #Lista prodotti in base al brand
    path('prodotto/<int:pk>/acquista/', views.acquista, name='acquista'), #Acquista
    path('checkout/<str:condizione>/<int:prodotto_pk>/', views.checkout, name='checkout'), #Checkout
    path('confirmed/<int:utente_pk>/<int:dettaglio_pk>', views.acquistoeffettuato, name='confermato'), #Conferma ordine

    #CRUD
    path('gestione', views.crud_operations, name="gestione"),

    path('createbrand', views.BrandCreateView.as_view(), name="brand_create"),
    path('createprodotto', views.ProdottoCreateView.as_view(), name="prodotto_create"),
    path('createdettaglio', views.DettaglioCreateView.as_view(), name="dettaglio_create"),
    path('createcomanda', views.ComandaCreateView.as_view(), name="comanda_create"),

    #path('updatebrand', views.BrandUpdateView.as_view(), name="brand_update")
    
]
