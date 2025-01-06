from celery import shared_task
import time
import random

@shared_task(bind=True, max_retries=3)
def add(self, x, y):
    scenario = random.randint(1, 4)
    
    try:
        if scenario == 1:
            time.sleep(2)
            return x + y
            
        elif scenario == 2:
            time.sleep(1)
            if self.request.retries < 2:
                raise ConnectionError("Temporary network error")
            return x + y
            
        elif scenario == 3:
            time.sleep(1)
            raise ValueError("Invalid input values")
            
        else:
            time.sleep(8)
            return x + y
            
    except ConnectionError as exc:
        raise self.retry(exc=exc, countdown=2)

@shared_task(bind=True, max_retries=3)
def multiply(self, x, y):
    scenario = random.randint(1, 4)
    
    try:
        if scenario == 1:
            time.sleep(2)
            return x * y
            
        elif scenario == 2:
            time.sleep(1)
            if self.request.retries < 2:
                raise TimeoutError("Operation timed out")
            return x * y
            
        elif scenario == 3:
            time.sleep(1)
            raise OverflowError("Number too large")
            
        else:
            time.sleep(8)
            return x * y
            
    except TimeoutError as exc:
        raise self.retry(exc=exc, countdown=2)

@shared_task(bind=True, max_retries=3)
def subtract(self, x, y):
    scenario = random.randint(1, 4)
    
    try:
        if scenario == 1:
            time.sleep(2)
            return x - y
            
        elif scenario == 2:
            time.sleep(1)
            if self.request.retries < 2:
                raise ConnectionError("Database connection error")
            return x - y
            
        elif scenario == 3:
            time.sleep(1)
            raise ValueError("Invalid operation")
            
        else:
            time.sleep(8)
            return x - y
            
    except ConnectionError as exc:
        raise self.retry(exc=exc, countdown=2)

@shared_task(bind=True, max_retries=3)
def divide(self, x, y):
    scenario = random.randint(1, 4)
    
    try:
        if scenario == 1:
            time.sleep(2)
            return x / y
            
        elif scenario == 2:
            time.sleep(1)
            if self.request.retries < 2:
                raise ConnectionError("Service unavailable")
            return x / y
            
        elif scenario == 3:
            time.sleep(1)
            if y == 0:
                raise ZeroDivisionError("Division by zero")
            return x / y
            
        else:
            time.sleep(8)
            if y == 0:
                raise ZeroDivisionError("Division by zero")
            return x / y
            
    except ConnectionError as exc:
        raise self.retry(exc=exc, countdown=2)