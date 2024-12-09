from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from shop.models import Comanda

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

@login_required
def dashboard(request):
    comande = Comanda.objects.filter(utente=request.user).order_by('-data_acquisto')
    return render(request, 'users/dashboard.html', {"comande":comande})

@login_required
def custom_logout(request):
    logout(request)
    return redirect('users:login')

