from django.urls import path
from . import views

app_name = 'sell'

urlpatterns = [
    path('', views.home, name="homesell"), #Home
    path('valutazione/', views.valutazione, name="valutazione"), # Form valutazione 
    path('valutazione/success/<str:valutazione>', views.success, name="success"), # Valutazione eseguita
]