FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY
WORKDIR /code/django_project

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code/

RUN python manage.py collectstatic --no-input --settings=django_project.settings.prod

CMD ["gunicorn", "django_project.wsgi:application", "--bind", "0.0.0.0:8000"]
