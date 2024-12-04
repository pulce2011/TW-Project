from django.db import models

# Brand di prodotti
class Brand(models.Model):
    nome = models.CharField(max_length=100, unique=True)  # Nome del brand
    immagine = models.CharField(max_length=20, unique=True) # Nome immagine all'interno di "brand_imgs"

    def __str__(self):
        return self.nome

# Prodotti
class Prodotto(models.Model):
    CONDITION_CHOICES = [
        ('new', 'Nuovo'),
        ('used', 'Usato'),
        ('refurbished', 'Ricondizionato'),
    ]

    nome = models.CharField(max_length=200)               # Nome del prodotto
    descrizione = models.TextField()                      # Descrizione completa
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)  # Prezzo del prodotto
    quantita = models.PositiveIntegerField(default=0)        # Quantità disponibile
    condizione = models.CharField(max_length=20, choices=CONDITION_CHOICES)  # Condizione
    modello = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='modello')  # Modello associata
    immagine = models.CharField(max_length=20, unique=True) # Nome immagine all'interno di "brand_imgs"
    data_pub = models.DateTimeField(auto_now_add=True)  # Data di ccreazione

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Prodotti"