from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Brand, Prodotto, Dettagli, Comanda
from .forms import CondizioneProdottoForm


class ShopModelTests(TestCase):

    def setUp(self):

        #Crea un brand di test
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
            prezzo=599.99,
            quantita=10,
        )

    def test_brand_creation(self):
        """Test per verificare che il brand sia stato creato correttamente"""
        self.assertEqual(self.brand.__str__(), "Test Brand")

    def test_prodotto_creation(self):
        """Test per verificare che il prodotto sia stato creato correttamente"""
        self.assertEqual(self.prodotto.__str__(), "Test Prodotto")

    def test_dettaglio_creation(self):
        """Test per verificare che il dettaglio sia stato creato correttamente"""
        self.assertEqual(
            self.dettaglio.__str__(),
            "Test Prodotto (new) - 10 disponibili"
        )


class ShopFormTests(TestCase):

    def test_condizione_prodotto_form_valid(self):
        """Test per Form acquisto valido"""
        form = CondizioneProdottoForm(data={
            'condizione': 'new',
            'memoria': 64,
        })

        self.assertTrue(form.is_valid())

    def test_condizione_prodotto_form_invalid(self):
        """Test per form acquisto NON valido"""
        form = CondizioneProdottoForm(data={})
        self.assertFalse(form.is_valid())


class ShopViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.brand = Brand.objects.create(nome="Test Brand")
        self.prodotto = Prodotto.objects.create(
            nome="Test Prodotto",
            descrizione="Descrizione di test",
            modello=self.brand,
        )


    def test_home_view(self):
        """Test per la vista 'home' """
        response = self.client.get(reverse('shop:homeshop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/home_shop.html')

    def test_all_products_view(self):
        """Test per la vista 'tutti i prodotti' """
        response = self.client.get(reverse('shop:prodotti'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/all_prodotti.html')

    def test_product_detail_view(self):
        """Test per la vista 'prodotto in dettaglio' """
        response = self.client.get(reverse('shop:product_detail', args=[self.prodotto.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/detail_product.html')

    def test_search_view(self):
        """Test per la vista 'cerca' """
        response = self.client.get(reverse('shop:search') + '?search=Test')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/all_prodotti.html')

    def test_acquista_view_authenticated(self):
        """Test per la vista 'acquista' con utente autenticato"""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('shop:acquista', args=[self.prodotto.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/acquista.html')

    def test_acquista_view_unauthenticated(self):
        """Test per la vista 'acquista' con utente NON autenticato"""
        response = self.client.get(reverse('shop:acquista', args=[self.prodotto.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to login
