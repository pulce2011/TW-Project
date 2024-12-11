# TW-Project

**TW-Project** è un portale e-commerce realizzato in Django per la vendita di telefoni cellulari usati, nuovi e ricondizionati, creato come progetto per l'esame di Tecnologie Web.

## **Funzionalità Principali**

- Registrazione e autenticazione per acquirenti e fornitori.
- Gestione prodotti: aggiunta, modifica e rimozione.
- Sezione di recensioni e valutazioni.
- Ricerca avanzata con filtri per brand, memoria, prezzo e condizione.
- Sistema di raccomandazioni basato sulle recensioni.
- Dashboard con statistiche di vendita.

---

## **Requisiti di Sistema**

- Python 3.8+
- Django 4.x
- SQLite (database predefinito, ma supporta PostgreSQL e MySQL)
- Bootstrap 5

## **Installazione**

1. Clona il repository:
   ```bash
   git clone https://github.com/pulce2011/TW-Project.git
   ```

2. Entra nella directory del progetto:
   ```bash
   cd TW-Project
   ```

3. Crea e attiva un ambiente virtuale:
   ```bash
   python -m venv env
   source env/bin/activate  # Su Windows: env\Scripts\activate
   ```

4. Installa le dipendenze richieste:
   ```bash
   pip install -r requirements.txt
   ```

5. Applica le migrazioni per creare il database:
   ```bash
   python manage.py migrate
   ```

6. Crea un superutente per accedere al pannello admin:
   ```bash
   python manage.py createsuperuser
   ```

7. Avvia il server di sviluppo:
   ```bash
   python manage.py runserver
   ```

8. Accedi all'applicazione su [http://localhost:8000](http://localhost:8000).

---

## **Struttura del Progetto**

- **rplab/**: Directory principale del progetto.
- **sell/**: Gestisce la logica del portale e-commerce (prodotti, recensioni, dashboard, ecc.).
- **users/**: Gestisce l'autenticazione e il profilo degli utenti.
- **templates/**: Contiene i file HTML per il frontend.
- **static/**: File statici come CSS, JS e immagini.

---

## **Testing**

Il progetto include una suite di test automatizzati per garantire la stabilità e la correttezza delle funzionalità.

- Per eseguire i test:
  ```bash
  python manage.py test
  ```

- File dei test principali:
  - `sell/tests.py`
  - `users/tests.py`

---

## **Autori**

- Creatore: **[Filippo](mailto:filippofifafut@gmail.com)**
- Supervisore: **Prof. [Nome Cognome]**

---

## **Licenza**

Questo progetto è distribuito sotto licenza MIT. Consulta il file `LICENSE` per maggiori dettagli.
