from django.contrib import admin
from django.urls import path, include
from .views import *
from .initcmds import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), #HomePage
    path('home/', home, name='home'), #HomePage
    path('servizi/', servizi, name="servizi"), #Servizi
    path('about/', about, name="about"), #Chi siamo
    path('contatti/', contatti, name="contatti"), #Contatti

    path('shop/', include('shop.urls')), #Shop App

]

erase_db()
init_database()