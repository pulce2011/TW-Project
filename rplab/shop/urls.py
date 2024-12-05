from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Homepage dello shop
    path('', views.home, name='shop_home'),
    path('prodotti/', views.AllProdcutsListView.as_view(), name="prodotti"),
    path('brands/', views.AllBrandsListView.as_view(), name="brands"),
    path('prodotto/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('prodotto/<int:pk>/acquista/', views.acquista, name='acquista'),
    path('checkout/<str:condizione>/<int:prodotto_pk>/', views.checkout, name='checkout')
]
