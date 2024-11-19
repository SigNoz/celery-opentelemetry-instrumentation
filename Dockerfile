# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY requirements.txt ./
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5672 for RabbitMQ (optional)
EXPOSE 5672

# Define environment variables for OpenTelemetry
ENV OTEL_TRACES_EXPORTER=otlp
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
ENV OTEL_SERVICE_NAME=celery-app

# Run the Celery worker
CMD ["celery", "-A", "celery_app", "worker", "--loglevel=info"]
