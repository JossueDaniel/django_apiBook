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

## Configuración y ejecución
### 1. Clonar el repositorio
```bash
git clone https://github.com/JossueDaniel/django_apiBook.git
```

```bash
cd django_apiBook
```

### 2. Establecer las variables de entorno
Crear un archivo .env en la raíz del proyecto
```plaintext
SECRET_KEY=clave-secreta-django
```
