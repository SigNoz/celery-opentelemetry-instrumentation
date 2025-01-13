FROM python:3.9-alpine

# Set environment variables to avoid interactive prompts during package installation
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

# Install dependencies and vim
RUN apk add --no-cache \
    vim \
    build-base \
    gcc \
    musl-dev \
    libffi-dev \
    && pip install --upgrade pip

# Set the working directory
WORKDIR /code

# Copy requirements and install Python dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Install OpenTelemetry dependencies
RUN pip install opentelemetry-distro opentelemetry-instrumentation
RUN opentelemetry-bootstrap --action=install

# Copy application code
COPY . /code/celery_app/
RUN mv /code/celery_app/tasks /code/tasks

# Copy and set entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint and default command
ENTRYPOINT ["/entrypoint.sh"]
CMD ["opentelemetry-instrument", "celery", "-A", "celery_app.celery:app", "worker", "--loglevel=info", "-Q", "queue1,queue2,queue3,queue4"]
