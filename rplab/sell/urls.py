from django.urls import path
from . import views

app_name = 'sell'

urlpatterns = [
    path('', views.home, name="homesell"),
    path('valutazione/', views.valutazione, name="valutazione"),
    path('valutazione/success', views.success, name="success"),
]