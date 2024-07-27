FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install --upgrade pip

COPY requirements.txt /src/

RUN pip install -r requirements.txt

COPY . /src/
