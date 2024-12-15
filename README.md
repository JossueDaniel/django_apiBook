# Django_ApiBook
Este proyecto es un aplicación web que está desarrollado con python y Django que proporciona puntos de accesso (endpoints) a usuarios o sistemas que quieran interactuar con los datos de un sistema que registra la información de autores y sus libros mediante una API, la aplicación web y la base de datos se ejecutan en contenedores Docker para facilitar el desarrollo y despliegue..

## Características
- Exposición de una API RESTful para interactuar con los datos con Django Rest Framework.
- Persistencia de datos en PostgreSQL.
- Contenedores Docker para ejecutar tanto la aplicación como la base de datos.
- Uso de docker-compose para una configuración sencilla de los servicios.

## Requisitos previos
- python 3.8 o superior
- docker
- docker-compose

## Estructura del proyecto
```plaintext
django_apiBook/
├── Dockerfile
├── compose.yml
├── requirements.txt
└── django_project/
    ├── manage.py
    ├── apis/
    ├── book/
    ├── pages/
    ├── static/
    ├── templates/
    └── django_project/
        └── settings/
            ├── base.py
            ├── local.py
            └── prod.py
```
