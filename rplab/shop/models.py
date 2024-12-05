from django.db import models

# Brand di prodotti
class Brand(models.Model):
    nome = models.CharField(max_length=100, unique=True)  # Nome del brand
    immagine = models.CharField(max_length=20, unique=True) # Nome immagine

    def __str__(self):
        return self.nome

# Prodotti
class Prodotto(models.Model):
    nome = models.CharField(max_length=200)               # Nome del prodotto
    descrizione = models.TextField()                      # Descrizione completa
    modello = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='modello')  # Brand associato
    immagine = models.CharField(max_length=20, unique=True) # Nome immagine all'interno di "brand_imgs"
    data_pub = models.DateTimeField(auto_now_add=True)  # Data di ccreazione

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
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)  # Prezzo del prodottoe
    quantita = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('prodotto', 'condizione')  # Garantisce che ogni combinazione prodotto-condizione sia unica
        verbose_name_plural = "Quantità Prodotto"

    def __str__(self):
        return f"{self.prodotto.nome} ({self.condizione}) - {self.quantita} disponibili"
        