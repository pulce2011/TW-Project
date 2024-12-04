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
        "nome": ["Apple"],
        "img": ["apple.png"],
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
    }

    #Creiamo i brand e associamo il nome
    for b in range(1):
        new_brand = Brand()
        new_brand.nome = brands["nome"][b]
        new_brand.immagine = brands["img"][b]
        new_brand.save()

        #Per ciascun brand creiamo 5 prodotti
        for p in range(5):
            new_product = Prodotto()
            new_product.nome = products["nome"][p]
            new_product.descrizione = products["descrizione"][p]
            new_product.prezzo = products["prezzo"][p]
            new_product.quantita = products["quantita"][p]
            new_product.condizione = products["condizione"][p]
            new_product.modello = new_brand
            new_product.immagine = new_product.nome.replace(" ", "").lower()+".png"
            new_product.data_pub = timezone.now()
            new_product.save()

    print("[LOG] Brands: " + str(Brand.objects.all())) #controlliamo
    print("[LOG] Prodotti: " + str(Prodotto.objects.all()))
