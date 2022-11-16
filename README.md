# Проект API_Yamdb с использованием DOCKER

![yamdb_workflow](https://github.com/shogun500/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Страницы проекта:

<a href=http://84.201.154.23/admin/> - Администрирование </a> <br>
<a href=http://84.201.154.23/api/v1/> - Страница запросов </a> <br>
<a href=http://84.201.154.23/redoc/> - Адрес сайта </a> <br>

# Как запустить проект:
## Создайте и заполните по образцу .env-файл
```
DB_ENGINE=<...>
DB_NAME=<...>
POSTGRES_USER=<...>
POSTGRES_PASSWORD=<...>
DB_HOST=<...>
DB_PORT=<...>
SECRET_KEY=<...>
```
## Собрать и запустить контейнер с помощью Docker-compose
```
docker-compose up --build
```
## Выполнить миграции через Docker-compose
```
docker-compose exec web python manage.py migrate --noinput
```
## Собрать через Docker-compose статику
```
docker-compose exec web python manage.py collectstatic --no-input
```
## Создать суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```
## Заполнить базу начальными данными
```
docker cp fixtures.json <CONTAINER_ID>:/app/fixtures.json
docker-compose exec web python manage.py loaddata fixtures.json
```


## Используемые технологии
![Alt-Текст](https://img.shields.io/badge/python-3.8-blue)
![Alt-Текст](https://img.shields.io/badge/django-2.2.16-blue)
![Alt-Текст](https://img.shields.io/badge/djangorestframework-3.12.4-blue)
![Alt-Текст](https://img.shields.io/badge/docker-20.10.16-blue)
![Alt-Текст](https://img.shields.io/badge/nginx-1.21.3-blue)
![Alt-Текст](https://img.shields.io/badge/gunicorn-20.0.4-blue)

## Автор

<a href=https://github.com/shogun500>Sergey Pavlov</a>
