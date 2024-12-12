from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from shop.models import Brand, Prodotto, Dettagli
from sell.models import Valutazione
from decimal import Decimal

class SellAppTests(TestCase):

    def setUp(self):
        # Crea un utente di test
        self.user = User.objects.create_user(username="testuser", password="password")

        # Crea un brand di test
        self.brand = Brand.objects.create(nome="Test Brand", immagine="brands/test.png")

        # Crea un prodotto di test
        self.prodotto = Prodotto.objects.create(
            nome="Test Prodotto",
            immagine="prodotti/test.png",
            descrizione="Descrizione di test",
            modello=self.brand,
        )

        # Crea un dettaglio di test
        self.dettaglio = Dettagli.objects.create(
            prodotto=self.prodotto,
            condizione='new',
            memoria=64,
            prezzo=Decimal(599.99),
            quantita=10,
        )

        # URL per il form di valutazione
        self.valutazione_url = reverse('sell:valutazione')

        # Client autenticato
        self.client = Client()
        self.client.login(username="testuser", password="password")

    def test_home_sell_view(self):
        """Test per la vista home_sell."""
        response = self.client.get(reverse('sell:homesell'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sell/home_sell.html")

    def test_valutazione_form_valid_data(self):
        """Test per il form di valutazione con dati validi."""
        form_data = {
            "prodotto": self.prodotto.id,
            "memoria": 64,
            "condizione": "excellent",
            "schermo_rotto": False,
            "back_rotto": False,
            "stato_batteria": 100,
            "bloccato": False,
            "commento": "Nessun difetto."
        }

        response = self.client.post(self.valutazione_url, form_data)

        # Controlla che il redirect sia avvenuto correttamente
        self.assertEqual(response.status_code, 302)

        # Controlla che il record sia stato creato
        valutazione = Valutazione.objects.get(prodotto=self.prodotto.id)
        self.assertIsNotNone(valutazione)
        self.assertAlmostEqual(valutazione.valore, self.dettaglio.prezzo*Decimal(0.9), places=2)  # 90% del prezzo originale

    def test_valutazione_form_invalid_data(self):
        """Test per il form di valutazione con dati non validi."""
        form_data = {
            "prodotto": self.prodotto.id,
            "memoria": 64,
            "condizione": "excellent",
            "schermo_rotto": False,
            "back_rotto": False,
            "stato_batteria": 150,  # Stato batteria non valido
            "bloccato": False,
            "commento": "Nessun difetto."
        }

        response = self.client.post(self.valutazione_url, form_data)
        
        # Verifica che la risposta non sia un redirect (resta sulla pagina con errori)
        self.assertEqual(response.status_code, 200)

        # Verifica che il form sia presente nel contesto
        self.assertIn('form', response.context)

        # Controlla gli errori del form
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('stato_batteria', form.errors)
        self.assertEqual(form.errors['stato_batteria'][0], "Ensure this value is less than or equal to 100.")

    def test_success_view(self):
        """Test per la vista di successo."""
        response = self.client.get(reverse('sell:success', args=[Decimal(900)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sell/success.html")
        self.assertContains(response, "900.00")