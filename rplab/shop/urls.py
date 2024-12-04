from django.urls import path
from . import views

urlpatterns = [
    # Homepage dello shop
    path('', views.home, name='shop_home'),

]
