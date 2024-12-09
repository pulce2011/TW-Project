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

    #Create
    path('createbrand', views.BrandCreateView.as_view(), name="brand_create"),
    path('createprodotto', views.ProdottoCreateView.as_view(), name="prodotto_create"),
    path('createdettaglio', views.DettaglioCreateView.as_view(), name="dettaglio_create"),
    path('createcomanda', views.ComandaCreateView.as_view(), name="comanda_create"),

    #Update
    path('select-brand-to-update', views.select_brand_to_update, name="brand_update"),
    path('select-prodotto-to-update', views.select_prodotto_to_update, name="prodotto_update"),
    path('select-dettaglio-to-update', views.select_dettaglio_to_update, name="dettaglio_update"),
    path('select-comanda-to-update', views.select_comanda_to_update, name="comanda_update"),

    path('updatebrand/<int:pk>', views.BrandUpdateView.as_view(), name="selected_brand_update"), 
    path('updateprodotto/<int:pk>', views.ProdottoUpdateView.as_view(), name="selected_prodotto_update"),
    path('updatedettaglio/<int:pk>', views.DettaglioUpdateView.as_view(), name="selected_dettaglio_update"),
    path('updatecomanda/<int:pk>', views.ComandaUpdateView.as_view(), name="selected_comanda_update"),

    #Delete
    path('delete-brand-to-update', views.select_brand_to_delete, name="brand_delete"),
    path('delete-prodotto-to-update', views.select_prodotto_to_delete, name="prodotto_delete"),
    path('delete-dettaglio-to-update', views.select_dettaglio_to_delete, name="dettaglio_delete"),
    path('delete-comanda-to-update', views.select_comanda_to_delete, name="comanda_delete"),

    path('deletebrand/<int:pk>', views.BrandDeleteView.as_view(), name="selected_brand_delete"), 
    path('deleteprodotto/<int:pk>', views.ProdottoDeleteView.as_view(), name="selected_prodotto_delete"),
    path('deletedettaglio/<int:pk>', views.DettaglioDeleteView.as_view(), name="selected_dettaglio_delete"),
    path('deletecomanda/<int:pk>', views.ComandaDeleteView.as_view(), name="selected_comanda_delete"),
    
]
