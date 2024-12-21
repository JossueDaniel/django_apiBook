FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/django_project

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code/

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "django_project.wsgi:application", "--bind", "0.0.0.0:8000"]
