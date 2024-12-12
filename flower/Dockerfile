FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN pip install flower

COPY . /code/

EXPOSE 5555

CMD ["celery", "--broker=amqp://guest:guest@localhost:5672//", "flower"]