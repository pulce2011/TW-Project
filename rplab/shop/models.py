from django.db import models
from django.contrib.auth.models import User
import os


# Rinominare immagine brand e salvarla in percorso specifico

def rename_brand_image(instance):
    base_filename = instance.nome.replace(' ', '').lower()
    new_filename = f"{base_filename}.png"
    return os.path.join('shop/static/brands', new_filename)


# Rinominare immagine prodotto e salvarla in percorso specifico

def rename_product_image(instance):
    base_filename = instance.nome.replace(' ', '').lower()
    new_filename = f"{base_filename}.png"
    return os.path.join('shop/static/prodotti', new_filename)


# Brand

class Brand(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    immagine = models.ImageField(upload_to=rename_brand_image)

    def __str__(self):
        return self.nome


# Prodotto

class Prodotto(models.Model):
    nome = models.CharField(max_length=200)
    descrizione = models.TextField()
    modello = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='modello')
    immagine = models.ImageField(upload_to=rename_product_image)
    data_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Prodotti"
        

# Possibili condizioni di prodotto

class Condizione(models.TextChoices):
    new = 'new', 'Nuovo'
    used = 'used', 'Usato'
    refurbished = 'refurbished', 'Ricondizionato'


# Possibili memorie di prodotto

class Memorie(models.IntegerChoices):
    GB_64 = 64, '64 GB'
    GB_128 = 128, '128 GB'
    GB_256 = 256, '256 GB'
    GB_512 = 512, '512 GB'
    TB_1 = 1024, '1 TB'

# Prodotto in dettaglio

class Dettagli(models.Model):
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE, related_name='prodotto')
    condizione = models.CharField(max_length=15, choices=Condizione.choices)
    memoria = models.PositiveIntegerField(choices=Memorie.choices)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    quantita = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('prodotto', 'condizione', 'memoria')
        verbose_name_plural = "Dettagli Prodotto"

    def __str__(self):
        return f"{self.prodotto.nome} ({self.condizione}) - {self.quantita} disponibili"
        

#Ordini effettuati

class Comanda(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="utente")
    dettagli = models.ForeignKey(Dettagli, on_delete=models.CASCADE, related_name="prodotto_dettaglio")  # Dettagli dell'acquisto (condizione, prezzo)
    data_acquisto = models.DateTimeField(auto_now_add=True)
    completata = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return f"{self.id}: Acquisto di '{self.dettagli.prodotto.nome}' da '{self.utente.username}'"

    class Meta:
        verbose_name_plural = "Comande"