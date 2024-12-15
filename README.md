# RPLab Electronic Service

Applicazione django per la vendita e la valutazione di telefoni cellulari nuovi, usati e ricondizionati.

## Installazione

1. Clona la repository corrente ed entra nella cartella del progetto.
```
git clone <url_repository> && cd TW-Project/rplab
```
2. Entrare nella cartella del progetto e verificare di avere installato python e le sue impostazioni (pip)
```
python --version
```
3. Attivare la shell per creare un venv pip tramite:
```
pipenv shell
```
4. Installare l'estensione di django:
```
pip install django
```
5. Eseguire la migrazione per configurare tutti i database:
```
python manage.py migrate
```
6. Avviare il server:
```
python manage.py runserver
```
