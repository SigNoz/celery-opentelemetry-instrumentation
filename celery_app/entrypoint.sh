#!/bin/sh

# Perform any necessary modifications here
echo "Performing pre-execution tasks..."

# Introduce a delay (e.g., 10 seconds)
echo "Waiting for 60 seconds before starting the Celery worker starts..."
sleep 60

# Execute the main command passed as arguments to the script
exec "$@"

