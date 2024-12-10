from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .initcmds import *

urlpatterns = [
    path('admin/', admin.site.urls), #AdminPage
    path('', home, name='home'), #HomePage
    path('home/', home, name='home'), #HomePage
    path('servizi/', servizi, name="servizi"), #Servizi
    path('about/', about, name="about"), #About
    path('contatti/', contatti, name="contatti"), #Contatti

    path('shop/', include('shop.urls')), #Shop App
    path('users/', include('users.urls')),  # Users App

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#erase_db()
init_database()