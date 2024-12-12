FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gcc

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN pip install opentelemetry-distro
RUN pip install opentelemetry-instrumentation
RUN opentelemetry-bootstrap --action=install

COPY . /code/

CMD ["opentelemetry-instrument", "python", "generator1.py"]