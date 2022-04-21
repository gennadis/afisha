UP
```bash
docker-compose -f docker-compose.yaml up -d --build
```

DOWN
```bash
docker-compose -f docker-compose.yaml down
```


Run the migrations and collect static files:
==> look for `entrypoint.sh` ==>
```bash
docker-compose -f docker-compose.yaml exec web python manage.py migrate
docker-compose -f docker-compose.yaml exec web python manage.py collectstatic --no-input --clear
docker-compose -f docker-compose.yaml exec web python manage.py createsuperuser
```
Check the logs:
```bash
docker-compose -f docker-compose.yaml logs -f
```
