# users/tests/test_users.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from shop.models import Comanda, Brand, Prodotto, Dettagli
from sell.models import Valutazione
from django.utils import timezone
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.auth.models import User
from decimal import Decimal

class UserRegistrationTestCase(TestCase):
    
    def test_register_user(self):
        """Test per registrazione utenti"""

        register_data = {
            'first_name': 'Mario',
            'last_name': 'Rossi',
            'username': 'mrossi',
            'email': 'validuser@example.com',
            'numero_di_telefono': '1234567890',
            'password1': 'pulcepepe123',
            'password2': 'pulcepepe123',
        }

        # Vai alla pagina di login e invia la richiesta
        url = reverse('users:register')
        response = self.client.post(url, register_data)

        # Cerca di recuperare l'utente
        user = get_user_model().objects.filter(username='mrossi').first()
        self.assertIsNotNone(user)  # Verifica che l'utente sia stato creato
        
        # Verifica che la redirezione avvenga correttamente
        self.assertRedirects(response, reverse('users:login'))


class UserLoginTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='mrossi', password='password123') #Utente registrato

    def test_login_user(self):
        """Test per login utenti"""

        login_data = {
            'username': 'mrossi',
            'password': 'password123'
        }
        
        # Vai alla pagina di login e invia la richiesta
        url = reverse('users:login')
        response = self.client.post(url, login_data, follow=True)
        
        # Verifica che l'utente sia loggato
        self.assertTrue(response.context['user'].is_authenticated)

        # Verifica che la redirezione avvenga correttamente
        self.assertRedirects(response, reverse('shop:homeshop'))

    def test_logout(self):
        """Test di logout"""
        self.client.login(username='mrossi', password='password123')
        response = self.client.get(reverse('users:logout'))
        self.assertRedirects(response, reverse('users:login'))  # Dopo il logout, redirect alla pagina di login


class UserDashboardTestCase(TestCase):

    def setUp(self):

        # Crea un utente di test
        self.user = User.objects.create_user(username='mrossi', password='password123')

        # Login utente
        self.client.login(username='mrossi', password='password123')

        # Crea un brand di test
        self.brand = Brand.objects.create(nome="testBrand",
                                          immagine="brands/test.png")
        
        # Crea un prodotto di test
        self.prodotto = Prodotto.objects.create(nome="testProdotto",
                                                modello=self.brand,
                                                descrizione="Test",
                                                immagine="prodtti/test.png",
                                                data_pub=timezone.now())
        
        # Crea un dettaglio di test
        self.dettagli = Dettagli.objects.create(prodotto=self.prodotto,
                                                condizione="new",
                                                memoria=64,
                                                prezzo=Decimal(100),
                                                quantita=3)
        
        # Crea una comanda di test
        Comanda.objects.create(utente=self.user,
                               dettagli=self.dettagli,
                               data_acquisto=timezone.now(),
                               completata=False)
        
        # Crea una valutazione di test
        Valutazione.objects.create(utente=self.user,
                                   prodotto=self.prodotto,
                                   memoria=64,
                                   condizione="excellent",
                                   schermo_rotto=False,
                                   back_rotto=False,
                                   stato_batteria=99,
                                   bloccato=False,
                                   commento="Nessun guasto.",
                                   completata=False)

    def test_dashboard_display_user(self):
        """Test della dashboard per un utente loggato"""

        response = self.client.get(reverse('users:dashboard'))
        self.assertContains(response, 'testBrand')
        self.assertContains(response, 'testProdotto')


class UserCRUDTestCase(TestCase):

    def setUp(self):
        """Impostazioni per test CRUD utente"""
        self.staff_user = User.objects.create_user(username='staff', password='staffpassword')
        self.staff_user.is_staff = True
        self.staff_user.save()
        self.client.login(username='staff', password='staffpassword')

    def test_user_list_view(self):
        """Test della vista che mostra tutti gli utenti (staff only)"""
        response = self.client.get(reverse('users:userlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_list.html')

    def test_user_detail_view(self):
        """Test della vista di dettaglio dell'utente"""
        response = self.client.get(reverse('users:userdetail', args=[self.staff_user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_detail.html')

    def test_user_update_view(self):
        """Test della vista di aggiornamento utente"""
        response = self.client.get(reverse('users:userupdate', args=[self.staff_user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/modifica_utente.html')


class UserUpdateViewTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='mrossi', password='password123')
        self.client.login(username='mrossi', password='password123')

    def test_user_update(self):
        """Test per la modifica delle informazioni utente"""
        data = {
            'username': 'newusername',
            'first_name': 'New',
            'last_name': 'Name',
            'email': 'new.email@example.com'
        }
        response = self.client.post(reverse('users:userupdate', args=[self.user.id]), data)
        self.assertRedirects(response, reverse('users:userlist'))  # Dopo la modifica, ritorna alla lista utenti
        self.user.refresh_from_db()  # Ricarica i dati dal database
        self.assertEqual(self.user.username, 'newusername')
        self.assertEqual(self.user.email, 'new.email@example.com')
