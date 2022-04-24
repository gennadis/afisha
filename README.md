# Afisha Service
This project helps maintaining information about local sights: location, description, photos, etc.
You can install and run it locally or use [deployed project](http://62.109.2.234:1337)

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
DJANGO_DEBUG=1
DJANGO_SECRET_KEY=secret_key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
CSRF_TRUSTED_ORIGINS=http://localhost:1337

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_dev
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
```

- Rename `example.env.db` to `.env.db` and fill it accordingly
```bash
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
POSTGRES_DB=hello_django_dev
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

6. Open `Places` app admin panel in browser [http://localhost:1337/admin/](http://localhost:1337/admin/)

7. Open frontend in browser [http://localhost:1337](http://localhost:1337)
