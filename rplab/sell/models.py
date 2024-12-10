from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from shop.models import Prodotto
from django.contrib.auth.models import User

class condizioni(models.TextChoices):
    EXCELLENT = "excellent", "Eccellente"
    GOOD = "good", "Buono"
    FAIR = "fair", "Discreto"
    DAMAGED = "damaged", "Danneggiato"
    NOT_WORKING = "not_working", "Non funzionante"


class Valutazione(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    memoria = models.PositiveIntegerField(help_text="Capacità di memoria in GB")
    condizione = models.CharField(max_length=20, choices=condizioni.choices)
    schermo_rotto = models.BooleanField(default=False, help_text="Lo schermo è rotto?")
    back_rotto = models.BooleanField(default=False, help_text="Ha il vetro posteriore rotto?")
    stato_batteria = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], help_text="Qual è lo stato batteria?")
    bloccato = models.BooleanField(default=False, help_text="Il telefono è bloccato dalla casa produttrice?")
    commento = models.CharField(blank=True, null=True, max_length=200, help_text="Aggiungi ulteriori commenti sullo stato del dispositivo")
    valore = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Valore stimato del dispositivo")

    def __str__(self):
        return f"Valutazione di {self.prodotto} - {self.condizione}"

    class Meta:
        verbose_name_plural = "Valutazioni"