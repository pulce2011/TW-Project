from django.db import models
from django.contrib.auth.models import User


# Brand di prodotti

class Brand(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    immagine = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome


# Prodotti

class Prodotto(models.Model):
    nome = models.CharField(max_length=200)
    descrizione = models.TextField()
    modello = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='modello')
    immagine = models.CharField(max_length=20, unique=True)
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


# Quantita per ogni prodotto in base alla condizione

class Dettagli(models.Model):
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE, related_name='prodotto')
    condizione = models.CharField(max_length=15, choices=Condizione.choices)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    quantita = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('prodotto', 'condizione')
        verbose_name_plural = "Quantità Prodotto"

    def __str__(self):
        return f"{self.prodotto.nome} ({self.condizione}) - {self.quantita} disponibili"
        

class Comanda(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="utente")
    dettagli = models.ForeignKey(Dettagli, on_delete=models.CASCADE, related_name="prodotto_dettaglio")  # Dettagli dell'acquisto (condizione, prezzo)
    data_acquisto = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: Acquisto di '{self.dettagli.prodotto.nome}' da '{self.utente.username}'"

    class Meta:
        verbose_name_plural = "Comande"