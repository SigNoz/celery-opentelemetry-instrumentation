from celery import shared_task
import time

@shared_task
def add(x, y):
    time.sleep(2)  # Simulate delay
    return x + y

@shared_task
def multiply(x, y):
    time.sleep(2)
    return x * y

@shared_task
def subtract(x, y):
    time.sleep(2)
    return x - y

@shared_task
def divide(x, y):
    time.sleep(2)
    if y == 0:
        raise ValueError("Division by zero!")
    return x / y