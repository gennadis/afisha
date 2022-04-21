# Afisha Service

This project helps with...
It maintains places locations, photos, etc... 
You can install and run it on your local machine or use already [deployed project](https://UPDATE_THIS_LINK)

![Demo](demo.gif)

# Docker intructions
1. Clone project
```bash
git clone https://github.com/gennadis/afisha.git
cd afisha
```

2. Rename `example.env` to `.env` and fill your secrets in it.  
```bash
DJANGO_DEBUG=0  # [0, 1]
DJANGO_SECRET_KEY=<secret>
DJANGO_ALLOWED_HOSTS=<host1 host2>  #localhost 127.0.0.1 [::1]

SQL_ENGINE=<engine>  # django.db.backends.postgresql
SQL_DATABASE=<database>
SQL_USER=<user>
SQL_PASSWORD=<password>
SQL_HOST=<host>
SQL_PORT=<port> # 5432
```

3. Rename `example.env.db` to `.env.db` and fill your secrets in it.  
```bash
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<db>
```

3. Build and spin up the containers  
Database migration and static collection processes are run automatically
```bash
docker compose -f docker-compose.yaml up -d --build
```

4. Create Django superuser
```bash
docker compose -f docker-compose.yaml exec web python manage.py createsuperuser
```


## Installation
1. Clone project
```bash
git clone https://github.com/gennadis/afisha.git
cd afisha
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Rename `example.env` to `.env` and fill your secrets in it.  
```bash
DJANGO_DEBUG=0  # [0, 1]
DJANGO_SECRET_KEY=<secret>
DJANGO_ALLOWED_HOSTS=<host1 host2>  #localhost 127.0.0.1 [::1]

SQL_ENGINE=<engine>  # django.db.backends.postgresql
SQL_DATABASE=<database>
SQL_USER=<user>
SQL_PASSWORD=<password>
SQL_HOST=<host>
SQL_PORT=<port> # 5432
```

5. Rename `example.env.db` to `.env.db` and fill your secrets in it.  
```bash
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<db>
```

6. Apply database migrations
```bash
python manage.py migrate
```

7. Create Django superuser
```bash
python manage.py createsuperuser
```

8. Run gunicorn web server
```bash
python manage.py runserver
```

# Usage
1. Open `Places` app admin panel in browser [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

2. Open frontend in browser [http://127.0.0.1:8000](http://127.0.0.1:8000)


