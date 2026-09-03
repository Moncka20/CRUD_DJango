# Biblioteca academica

CRUD de libros construido con Django, Bootstrap 5 y MariaDB/PyMySQL.

## Instalacion en Windows

```powershell
cd E:\TDSW\crud_Django
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py seed_books
python manage.py runserver
```

Abre http://127.0.0.1:8000/.

El proyecto usa SQLite por defecto para que pueda probarse sin MariaDB. Para MariaDB, crea la base de datos y configura `DB_ENGINE=mysql`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` y `DB_PORT` en `.env`.

## MariaDB

```sql
CREATE DATABASE biblioteca_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
GRANT ALL PRIVILEGES ON biblioteca_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

Despues ejecuta `python manage.py migrate`.

## Pruebas

```powershell
python manage.py test
```
