from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from shop.models import Comanda
from sell.models import Valutazione
from .forms import *
from .crud_views.create import *
from .crud_views.update import *
from .crud_views.delete import *


#Vista registrazione utente

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrazione completata! Ora puoi effettuare il login.')
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


#Vista dashboard utente

@login_required
def dashboard(request):
    comande = Comanda.objects.filter(utente=request.user).order_by('-data_acquisto')
    comande_attive = Comanda.objects.all().filter(attiva=True).order_by('-data_acquisto')
    valutazioni = Valutazione.objects.filter(utente=request.user).order_by('-id')
    valutazioni_attive = Valutazione.objects.all().filter(attiva=True).order_by('id')

    return render(request, 'users/dashboard.html', {"comande":comande,
                                                    "valutazioni":valutazioni,
                                                    "comande_attive":comande_attive,
                                                    "valutazioni_attive":valutazioni_attive,
                                                    })


#Vista logout utente

@login_required
def custom_logout(request):
    logout(request)
    return redirect('users:login')


# Vista tutte le comande
@staff_member_required
def all_comande_staff(request):
    comande = Comanda.objects.all()
    return render(request, 'users/staff_all_comande.html', {"comande_attive":comande,
                                                            "title":"Tutte le comande:"})
                                                                

# Vista tutte le valutazioni
@staff_member_required
def all_valutazioni_staff(request):
    valutazioni = Valutazione.objects.all()
    return render(request, 'users/staff_all_valutazioni.html', {"valutazioni_attive":valutazioni,
                                                            "title":"Tutte le valutazioni:"})


# Classe Lista Utenti

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'utente'


# Classe Dettaglio Utente
                                                    
class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'utente'


# Vista pagina homepage per le operazione CRUD

@staff_member_required
def crud_operations(request):
    operation = request.GET.get('operazione')
    model = request.GET.get('modello')

    if operation and model:
        url_name = f"{model}_{operation}" 
        print("URL_NAME: " + url_name) # Es: "brand_create"
        return redirect('users:' + url_name)
    else:
        return render(request, "users/CRUD/home_crud.html")


#Classe per la modifica di un utente

class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/modifica_utente.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    context_object_name = 'utente'

    def get_success_url(self):
        # Dopo la modifica, ritorna alla lista utenti
        return reverse_lazy('users:userlist')
