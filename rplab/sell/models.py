from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from shop.models import Prodotto
from django.contrib.auth.models import User
from shop.models import Memorie

class Condizioni(models.TextChoices):
    EXCELLENT = "excellent", "Eccellente"
    GOOD = "good", "Buono"
    FAIR = "fair", "Discreto"
    DAMAGED = "damaged", "Danneggiato"
    NOT_WORKING = "not_working", "Non funzionante"


class Valutazione(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    memoria = models.PositiveIntegerField(choices=Memorie.choices)
    condizione = models.CharField(max_length=20, choices=Condizioni.choices)
    schermo_rotto = models.BooleanField(default=False)
    back_rotto = models.BooleanField(default=False)
    stato_batteria = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    bloccato = models.BooleanField(default=False, help_text="Il telefono è bloccato dalla casa produttrice?")
    commento = models.CharField(blank=True, null=True, max_length=200, help_text="Aggiungi ulteriori commenti sullo stato del dispositivo")
    valore = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Valore stimato del dispositivo")
    completata = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return f"Valutazione di {self.prodotto} - Utente: *{self.utente.username}*"

    class Meta:
        verbose_name_plural = "Valutazioni"