FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

RUN apt-get update && apt-get install -y gcc

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN pip install opentelemetry-distro
RUN pip install opentelemetry-instrumentation
RUN opentelemetry-bootstrap --action=install

COPY . /code/celery_app/

CMD ["opentelemetry-instrument", "celery", "-A", "celery_app.celery:app", "worker", "--loglevel=info", "-Q", "queue1,queue2,queue3,queue4"]