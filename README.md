# Afisha Service
This project helps maintaining information about local sights: location, description, photos, etc.
You can install and run it locally or use deployed project:
- [fronend](http://62.109.2.234:1337)
- [backend](http://62.109.2.234:1337/admin)

![Demo](demo.gif)

## Docker intructions
1. Clone project
```bash
git clone https://github.com/gennadis/afisha.git
cd afisha
```

2. Prepare environment variables:  
- Rename `example.env` to `.env` and fill it accordingly
```bash
DJANGO_DEBUG=0                # [0, 1]
DJANGO_SECRET_KEY=<secret>
DJANGO_ALLOWED_HOSTS=<host1>  # localhost 127.0.0.1 [::1]

SQL_ENGINE=<engine>           # django.db.backends.postgresql
SQL_DATABASE=<database>
SQL_USER=<user>
SQL_PASSWORD=<password>
SQL_HOST=<host>
SQL_PORT=<port>               # 5432
```

- Rename `example.env.db` to `.env.db` and fill it accordingly
```bash
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<db>
```

3. Build and spin up the containers
*Database migration and static collection processes are run automatically*
```bash
docker compose -f docker-compose.yaml up -d --build
```

4. Create Django superuser
```bash
docker compose -f docker-compose.yaml exec web python manage.py createsuperuser
```

5. Load some data from `json` files:
```bash
docker compose -f docker-compose.yaml exec web python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Антикафе%20Bizone.json
```

The structure of `json` file:
```bash
{
    "title": "Останкинская телебашня",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e3b20361050ae13b3aaf7ddcef76e7c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/adc544d7acc9be889cfec73064bcfb06.jpg",
    ],
    "description_short": "Останкинская телебашня — одна из главных достопримечательностей Москвы...",
    "description_long": "<p>За последнее время внутри башни многое изменилось...</p>",
    "coordinates": {
        "lng": "37.61171499999998",
        "lat": "55.81972699999998"
    }
}
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

8. Run web server
```bash
python manage.py runserver
```
9. Open `Places` app admin panel in browser [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

10. Open frontend in browser [http://127.0.0.1:8000](http://127.0.0.1:8000)

