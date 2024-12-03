from django.shortcuts import render

#Vista per la homepage
def home(request):

    return render(request, template_name='home.html')

from django.shortcuts import render

#Vista per i servizi
def servizi(request):

    servizi = [
        {'nome': 'Riparazione Smartphone', 'descrizione': 'Ripariamo qualsiasi problema sul tuo smartphone.'},
        {'nome': 'Consulenza tecnica', 'descrizione': 'Supporto tecnico per tutti i tuoi dispositivi elettronici.'},
        {'nome': 'Vendita Ricondizionati', 'descrizione': 'Aiuta il pianeta acquistando un dispositivo ricondizionato da noi.'},
    ]
    return render(request, 'servizi.html', {'servizi': servizi})

from django.shortcuts import render

#Vista per 'Chi siamo'
def about(request):

    team = [
        {'nome':'Mario Rossi', 'ruolo':'Fondatore e CEO', 'descrizione':'Responsabile della visione e strategia aziendale.'},
        {'nome':'Giulia Bianchi', 'ruolo':'Responsabile Marketing','descrizione': 'Coordina tutte le attività di promozione e pubblicità.'},
        {'nome':'Luca Verdi', 'ruolo':'Tecnico Senior', 'descrizione': 'Specializzato in riparazioni e assistenza tecnica.'},
    ]

    team = [
        {'nome':'Irene Porcu', 'ruolo':'Fondatore e CEO', 'descrizione':'Responsabile della visione e strategia aziendale.'},
        {'nome':'Alessandro Doglia', 'ruolo':'Responsabile Marketing & Management','descrizione': 'Coordina tutte le attività di promozione, pubblicità e organizzazione.'},
        {'nome':'Flavio Roveri', 'ruolo':'Tecnico Senior', 'descrizione': 'Specializzato in riparazioni e microsaldatura a stagno'},
        {'nome':'Fabio Dall\'Olio', 'ruolo':'Tecnico Junior', 'descrizione':'Apprendista con grandi margini di miglioramento'},
        {'nome':'Filippo Cerchi', 'ruolo':'Tecnico Multifunzione', 'descrizione':'Specializzato in informatica e riparazione PC'}
    ]
    return render(request, 'about.html', {'team': team})
from django.shortcuts import render

def contatti(request):

    contatti = {
        'indirizzo': 'Via Cavour 38, Mirandola (MO), Italia',
        'email': 'info@rplabservice.it',
        'telefono': '+39 0535 1930015',
        'orari': 'Lun-Ven: 8:30-12.30 | 15.30-19:30'
    }
    return render(request, 'contatti.html', {'contatti': contatti})


