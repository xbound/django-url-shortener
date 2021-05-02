# Simple URL Shortener

URL shortener app written in Django.

## Setup

Install dependencies using [Poetry](https://python-poetry.org/):
```shell
$ poetry install
```
Run migrations:
```shell
$ poetry shell
$ cd django-url-shortener && python manage.py migrate
```
Create default superuser with username `admin` and password `12345678` use:
```shell
$ python manage.py create_default_admin
```
Start development server using `runserver` command:
```shell
$ python manage.py runserver
```

Application can also be started using `docker-compose`:
```shell
$ docker-compose up --build
```

Application will be available at http://127.0.0.1:8000/