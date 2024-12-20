from django.shortcuts import render


#Vista per la homepage

def home(request):

    return render(request, template_name='home.html')


#Vista per i servizi

def servizi(request):

    servizi = [
        {'nome': 'Riparazione Smartphone', 'descrizione': 'Ripariamo qualsiasi problema sul tuo smartphone.'},
        {'nome': 'Consulenza tecnica', 'descrizione': 'Supporto tecnico per tutti i tuoi dispositivi elettronici.'},
        {'nome': 'Vendita Ricondizionati', 'descrizione': 'Aiuta il pianeta acquistando un dispositivo ricondizionato da noi.'},
    ]
    return render(request, 'servizi.html', {'servizi': servizi})


#Vista per 'Chi siamo'

def about(request):

    team = [
        {'nome':'Irene Porcu', 'ruolo':'Fondatore e CEO', 'descrizione':'Responsabile della visione e strategia aziendale.'},
        {'nome':'Alessandro Doglia', 'ruolo':'Responsabile Marketing & Management','descrizione': 'Coordina tutte le attività di promozione, pubblicità e organizzazione.'},
        {'nome':'Flavio Roveri', 'ruolo':'Tecnico Senior', 'descrizione': 'Specializzato in riparazioni e microsaldatura a stagno'},
        {'nome':'Fabio Dall\'Olio', 'ruolo':'Tecnico Junior', 'descrizione':'Apprendista con grandi margini di miglioramento'},
        {'nome':'Filippo Cerchi', 'ruolo':'Tecnico Multifunzione', 'descrizione':'Specializzato in informatica e riparazione PC'}
    ]
    return render(request, 'about.html', {'team': team})


#Vista per i contatti

def contatti(request):

    contatti = {
        'indirizzo': 'Via Cavour 38, Mirandola (MO), Italia',
        'email': 'info@rplabservice.it',
        'telefono': '+39 0535 1930015',
        'orari': 'Lun-Ven: 8:30-12.30 | 15.30-19:30'
    }
    return render(request, 'contatti.html', {'contatti': contatti})


