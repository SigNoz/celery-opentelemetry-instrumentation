from celery import Celery
from opentelemetry.instrumentation.celery import CeleryInstrumentor

# Initialize Celery app
app = Celery('celery_app', broker='amqp://guest:guest@rabbitmq:5672//')

# Instrument Celery with OpenTelemetry
CeleryInstrumentor().instrument()

# Configuration (optional, for result backend)
app.conf.update(
    result_backend='rpc://',
)

if __name__ == "__main__":
    app.start()
