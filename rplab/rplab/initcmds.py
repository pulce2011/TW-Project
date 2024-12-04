from shop.models import Brand, Prodotto
from django.utils import timezone
from datetime import datetime, timedelta
from threading import Timer

def erase_db():
    Brand.objects.all().delete()
    Prodotto.objects.all().delete()


def init_database():

    if len(Brand.objects.all()) != 0:
        return
    
    # Inizializziamo 5 brand
    brands = {
        "nome": ["Apple", "Samsung"],
        "img": ["apple.png", "samsung.png"],
    }

    products = {
        "nome": ["iPhone 8", "iPhone X", "iPhone 11 Pro", "iPhone 12", "iPhone 14 Pro Max"],
        "descrizione":["Apple iPhone 8 è uno smartphone introdotto sul mercato nel 2017. E' dotato di una batteria da 1820 mAh ed integra al proprio interno fotocamere anteriore e posteriore rispettivamente da 7 megapixel e da 12 megapixel. Per quanto riguarda le dimensioni, abbiamo uno spessore di 67.3 mm, altezza di 138.4 mm e larghezza di 67.3 mm. Lo schermo, invece, si caratterizza per un pannello di tipo IPS (TFT) con diagonale di 4.7 pollici e risoluzione di 750x1334 pixel: anche in questo caso non cambiano le dimensioni dello schermo rispetto ai precedenti modelli della famiglia iPhone a partire dalla serie iPhone 6. Il processore equipaggiato è di tipo Hexa Core, modello Apple A11 Bionic, caratterizzato da una frequenza di clock pari a 2.5 GHz. La memoria di storage a disposizione parte da un minimo di 64 GB, con la possibilità di avere tagli superiori al variare del modello.",
                       "iPhone X è il rivoluzionario smartphone Apple del decimo anniversario. Sono passati dieci anni dal lancio dell'iPhone originale, e Apple innova rimuovendo una grossa parte delle cornici frontali. Il design è di tipo full-screen, con il display da 5,8 pollici finalmente AMOLED per la prima volta nella famiglia di smartphone Apple. iPhone X fa uso di un processore esa-core da 2,39 GHz, di 3 GB di RAM e di un doppio sistema fotografico per il posteriore con due moduli da 12 MP e stabilizzazione ottica. La batteria è da 2716 mAh e può essere caricata via wireless con accessori venduti separatamente rispetto alla dotazione d'acquisto.",
                       "Annunciato nel 2019, Apple iPhone 11 Pro è uno degli smartphone top di gamma dell'azienda americana. E' dotato di un display Super Retina XDR OLED con cornici di dimensioni ridotte, dalla risoluzione di 1125x2436 pixels e diagonale di 5,8 pollici. Il refresh rate è di 60Hz, mentre quale sistema operativo troviamo ovviamente il proprietario iOS al pari di tutti gli altri smartphone Apple.",
                       "Ha debuttato sul mercato nell'anno lo smartphone iPhone 12, uno tra i modelli di fascia più alta proposti da Apple. E' caratterizzato da un display Super Retina XDR OLED con diagonale di 6,1 pollici., dotato di cornici di dimensioni ridotte, che opera ad una risoluzione di 1170x2532 pixels con refresh rate di 60Hz. Il sistema operativo è quello proprietario iOS.",
                       "iPhone 14 Pro Max è uno degli smartphone top di gamma di Apple annunciati nel 2022. E' basato su un display Super Retina XDR OLED LTPO con cornici di dimensioni ridotte, dalla risoluzione di 1290x2796 pixel e diagonale di 6,7 pollici. Il refresh rate è di 120Hz, mentre quale sistema operativo troviamo il proprietario iOS."],
        "prezzo":[143.99, 216.49, 371, 283, 763.34],
        "quantita":[2, 5, 3, 1, 1],
        "condizione":["refurbished", "used", "new", "used", "new"],
    }, {
        "nome": ["Galaxy A52s", "Galaxy S22 Ultra", "Galaxy A12", "Galaxy Z Flip 3", "Galaxy S24 FE"],
        "descrizione":["Samsung Galaxy A52s è un smartphone Android di buon livello, fortemente votato all'imaging, in grado di soddisfare anche l'utente più esigente. Sorprende il display Touchscreen da 6.5 pollici che pone questo Samsung al vertice della categoria. Risoluzione di 2400x1080 pixel. Scorrendo la scheda tecnica di questo Samsung Galaxy A52s, notiamo che sul versante delle funzionalità non manca davvero nulla. A cominciare dal modulo 5G che permette un trasferimento dati e una navigazione in internet eccellente, passando per la connettività Wi-fi e il GPS. Questo Samsung Galaxy A52s è un prodotto con pochi competitor per ciò che riguarda la multimedialità grazie alla fotocamera da ben 64 megapixel che permette al Samsung Galaxy A52s di scattare foto di alta qualità con una risoluzione di 9238x6928 pixel e di registrare video in 4K alla risoluzione di 3840x2160 pixel. Che dire delle dimensioni: lo spessore di 8.4mm è contenuto e rende questo Samsung Galaxy A52s molto interessante. Il suo peso è di 189g e abbiamo 4500mAh per la batteria.",
                       "Samsung Galaxy S22 Ultra è uno smartphone Android con caratteristiche all'avanguardia che lo rendono una scelta eccellente per ogni tipo di utilizzo, rappresentando uno dei migliori dispositivi mobili mai realizzati. Dispone di un grande display da 6.8 pollici e di una risoluzione da 3080x1440 pixel, fra le più elevate attualmente in circolazione. Nello stilare la scheda tecnica di questo Samsung Galaxy S22 Ultra, notiamo che le funzionalità offerte sono innumerevoli e tutte al top di gamma. A cominciare dal modulo 5G che permette un trasferimento dati e una navigazione in internet eccellente, passando per la connettività Wi-fi e il GPS. La batteria è da 5000mAh.L'eccellenza di questo Samsung Galaxy S22 Ultra è completata da una fotocamera con un sensore da ben 108 megapixel che permette di scattare foto di alta qualità con una risoluzione di 12000x9000 pixel e di registrare video in 8K alla risoluzione di 7680x4320 pixel. Veniamo alle dimensioni: lo spessore di 8.9mm è contenuto e rende questo Samsung Galaxy S22 Ultra molto interessante. Il tutto sta in un oggetto dal peso di 229g.",
                       "Samsung Galaxy A12 è un smartphone Android di fascia media, con una scheda tecnica ideale per chi non ha troppe pretese ma che non vuole rinunciare ad un bel display touchscreen. Le funzioni offerte da questo Samsung Galaxy A12 sono più o meno quelle presenti su tutti i dispositivi più avanzati, a cominciare dalla connettività Wi-fi e dal GPS. Al top di gamma il trasferimento dati e la navigazione in internet grazie al modulo LTE 4G. Sorprende il display Touchscreen da 6.5 pollici che pone questo Samsung al vertice della categoria. Risoluzione di 1560x720 pixel. Questo Samsung Galaxy A12 è un prodotto con pochi competitor per ciò che riguarda la multimedialità grazie alla fotocamera da ben 48 megapixel che permette al Samsung Galaxy A12 di scattare foto fantastiche con una risoluzione di 8000x6000 pixel e di registrare video in alta definizione (Full HD) alla risoluzione di 1920x1080 pixel. Facendo un check sulle dimensioni, lo spessore di 8.9mm è contenuto e rende questo Samsung Galaxy A12 molto interessante. Il suo peso è di 205g e troviamo una batteria da 5000mAh.",
                       "Samsung Galaxy Z Flip 3 è un smartphone Android di buon livello, fortemente votato all'imaging, in grado di soddisfare anche l'utente più esigente. Sorprende il display Touchscreen da 6.7 pollici che pone questo Samsung al vertice della categoria. Risoluzione di 2640x1080 pixel. Scorrendo la scheda tecnica di questo Samsung Galaxy Z Flip 3, notiamo che sul versante delle funzionalità non manca davvero nulla. A cominciare dal modulo 5G che permette un trasferimento dati e una navigazione in internet eccellente, passando per la connettività Wi-fi e il GPS. Questo Samsung Galaxy Z Flip 3 è un prodotto con pochi competitor per ciò che riguarda la multimedialità grazie alla fotocamera da ben 12 megapixel che permette al Samsung Galaxy Z Flip 3 di scattare foto di buona qualità con una risoluzione di 4000x3000 pixel e di registrare video in 4K alla risoluzione di 3840x2160 pixel. Che dire delle dimensioni: lo spessore di appena 6.9mm rende questo Samsung Galaxy Z Flip 3 un prodotto completo e tra i più sottili sul mercato. Il suo peso è di 183g e abbiamo 3300mAh per la batteria.",
                       "Samsung Galaxy S24 FE è uno smartphone Android con caratteristiche all'avanguardia che lo rendono una scelta eccellente per ogni tipo di utilizzo, rappresentando uno dei migliori dispositivi mobili mai realizzati. Dispone di un grande display da 6.7 pollici e di una risoluzione da 2340x1080 pixel, fra le più elevate attualmente in circolazione. Nello stilare la scheda tecnica di questo Samsung Galaxy S24 FE, notiamo che le funzionalità offerte sono innumerevoli e tutte al top di gamma. A cominciare dal modulo 5G che permette un trasferimento dati e una navigazione in internet eccellente, passando per la connettività Wi-fi e il GPS. La batteria è da 4700mAh. L'eccellenza di questo Samsung Galaxy S24 FE è completata da una fotocamera con un sensore da ben 50 megapixel che permette di scattare foto di alta qualità con una risoluzione di 8165x6124 pixel e di registrare video in 8K alla risoluzione di 7680x4320 pixel. Veniamo alle dimensioni: lo spessore di 8mm è veramente contenuto e rende questo Samsung Galaxy S24 FE ancora più spettacolare. Il tutto sta in un oggetto dal peso di 213g."],
        "prezzo":[155, 339, 94.99, 539.99, 587.79],
        "quantita":[0, 4, 2, 8, 3],
        "condizione":["new", "refurbished", "used", "new", "refurbished"],
    }

    #Creiamo i brand e associamo il nome
    for b in range(2):
        new_brand = Brand()
        new_brand.nome = brands["nome"][b]
        new_brand.immagine = brands["img"][b]
        new_brand.save()

        #Per ciascun brand creiamo 5 prodotti
        for p in range(5):
            new_product = Prodotto()
            new_product.nome = products[b]["nome"][p]
            new_product.descrizione = products[b]["descrizione"][p]
            new_product.prezzo = products[b]["prezzo"][p]
            new_product.quantita = products[b]["quantita"][p]
            new_product.condizione = products[b]["condizione"][p]
            new_product.modello = new_brand
            new_product.immagine = new_product.nome.replace(" ", "").lower()+".png"
            new_product.data_pub = timezone.now()
            new_product.save()

    print("[LOG] Brands: " + str(Brand.objects.all())) #controlliamo
    print("[LOG] Prodotti: " + str(Prodotto.objects.all()))