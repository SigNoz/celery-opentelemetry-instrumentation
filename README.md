# Celery OpenTelemetry Instrumentation Demo

This project demonstrates how to instrument a Celery application with OpenTelemetry for distributed tracing and monitoring. It includes multiple task generators, workers, and a monitoring setup.

## Architecture

The project consists of the following components:

- **Celery Workers**: Process tasks from 4 different queues
- **Task Generators**: 4 separate services generating different mathematical operations
- **RabbitMQ**: Message broker for Celery
- **OpenTelemetry Collector**: Collects and exports telemetry data
- **Flower**: Web-based tool for monitoring Celery tasks

## Task Operations

- Queue1: Addition operation
- Queue2: Multiplication operation
- Queue3: Subtraction operation
- Queue4: Division operation

## Prerequisites

- Docker
- Docker Compose
- Python 3.9+ (for local development)

## Environment Variables

### Task Generators
- `CELERY_BROKER_URL`: RabbitMQ connection URL (default: `amqp://guest:guest@rabbitmq:5672//`)
- `TASK_DELAY`: Delay between task generation in seconds
  - Generator1: 10 seconds (default)
  - Generator2: 15 seconds (default)
  - Generator3: 20 seconds (default)
  - Generator4: 25 seconds (default)

### OpenTelemetry Configuration
- `OTEL_EXPORTER_OTLP_PROTOCOL`: Protocol for OpenTelemetry export
- `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`: Endpoint for logs
- `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`: Endpoint for metrics
- `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`: Endpoint for traces

## Setup and Running

1. Clone the repository:
```bash
git clone https://github.com/SigNoz/celery-opentelemetry-instrumentation.git
cd celery-opentelemetry-instrumentation
```

2. Build and start the services:
```bash
docker-compose up --build
```

3. Access the monitoring interfaces:
- Flower Dashboard: `http://localhost:5555`

## Project Structure

```
.
├── celery_app/
│   ├── celery.py          # Celery application configuration
│   └── Dockerfile         # Celery worker Dockerfile
├── task_generators/
│   ├── generator1.py      # Addition task generator
│   ├── generator2.py      # Multiplication task generator
│   ├── generator3.py      # Subtraction task generator
│   ├── generator4.py      # Division task generator
│   └── Dockerfile         # Task generators Dockerfile
├── tasks/
│   └── tasks.py           # Task definitions
├── opentelemetry-collector/
│   ├── config.yaml        # OpenTelemetry collector configuration
│   └── Dockerfile         # OpenTelemetry collector Dockerfile
└── docker-compose.yml     # Docker services configuration
```

## OpenTelemetry Configuration

The OpenTelemetry collector is configured to:
- Receive traces and metrics via OTLP (HTTP and gRPC)
- Process data using batch processor
- Export detailed debug information

## Celery Configuration

The Celery application is configured with:
- 4 separate queues (queue1, queue2, queue3, queue4)
- RPC result backend
- Task result expiration: 3600 seconds
- Default queue: queue1

## Development

To set up the development environment:

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r celery_app/requirements.txt
pip install -r task_generators/requirements.txt
```

## Monitoring and Debugging

- Use Flower dashboard to monitor task execution
- Check OpenTelemetry collector logs for trace information
- Monitor RabbitMQ queues for message flow

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request