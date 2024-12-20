from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.register, name='register'), # Registazione utente
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), # Login utente
    path('logout/', views.custom_logout, name='logout'), # Logout
    path('dashboard/', views.dashboard, name='dashboard'), # Dashboard
    path('comande/', views.all_comande_staff, name='allcomande'), # Tutte le comande (staff_only)
    path('valutazioni/', views.all_valutazioni_staff, name='allvalutazioni'), # Tutte le valutazioni (staff_only)
    path('', views.UserListView.as_view(), name='userlist'),  #Tutti gli utenti (staff_only)
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='userdetail'), # Dettagli utente
    path('users/<int:pk>/edit/', views.UserUpdateView.as_view(), name='userupdate'), # Modifica utente

    # CRUD HomePage
    path('gestione', views.crud_operations, name="gestione"),

    # Create
    path('createbrand', views.BrandCreateView.as_view(), name="brand_create"),
    path('createprodotto', views.ProdottoCreateView.as_view(), name="prodotto_create"),
    path('createdettaglio', views.DettaglioCreateView.as_view(), name="dettaglio_create"),
    path('createcomanda', views.ComandaCreateView.as_view(), name="comanda_create"),
    path('createvalutazione', views.ValutazioneCreateView.as_view(), name="valutazione_create"),

    # Select model to update
    path('select-brand-to-update', views.select_brand_to_update, name="brand_update"),
    path('select-prodotto-to-update', views.select_prodotto_to_update, name="prodotto_update"),
    path('select-dettaglio-to-update', views.select_dettaglio_to_update, name="dettaglio_update"),
    path('select-comanda-to-update', views.select_comanda_to_update, name="comanda_update"),
    path('select-valutazione-to-update', views.select_valutazione_to_update, name="valutazione_update"),

    # Update
    path('updatebrand/<int:pk>', views.BrandUpdateView.as_view(), name="selected_brand_update"), 
    path('updateprodotto/<int:pk>', views.ProdottoUpdateView.as_view(), name="selected_prodotto_update"),
    path('updatedettaglio/<int:pk>', views.DettaglioUpdateView.as_view(), name="selected_dettaglio_update"),
    path('updatecomanda/<int:pk>', views.ComandaUpdateView.as_view(), name="selected_comanda_update"),
    path('updatevalutazione/<int:pk>', views.ValutazioneUpdateView.as_view(), name="selected_valutazione_update"),

    # Select model to delete
    path('delete-brand-to-update', views.select_brand_to_delete, name="brand_delete"),
    path('delete-prodotto-to-update', views.select_prodotto_to_delete, name="prodotto_delete"),
    path('delete-dettaglio-to-update', views.select_dettaglio_to_delete, name="dettaglio_delete"),
    path('delete-comanda-to-update', views.select_comanda_to_delete, name="comanda_delete"),
    path('delete-valutazione-to-update', views.select_valutazione_to_delete, name="valutazione_delete"),


    # Delete
    path('deletebrand/<int:pk>', views.BrandDeleteView.as_view(), name="selected_brand_delete"), 
    path('deleteprodotto/<int:pk>', views.ProdottoDeleteView.as_view(), name="selected_prodotto_delete"),
    path('deletedettaglio/<int:pk>', views.DettaglioDeleteView.as_view(), name="selected_dettaglio_delete"),
    path('deletecomanda/<int:pk>', views.ComandaDeleteView.as_view(), name="selected_comanda_delete"),
    path('deletevalutazione/<int:pk>', views.ValutazioneDeleteView.as_view(), name="selected_valutazione_delete"),
]
