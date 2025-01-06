import time
import os
import random
from celery import Celery

broker_url = os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')
app = Celery('task_generators', broker=broker_url, backend='rpc://')

def generate_tasks(delay):
    while True:
        # Generate numbers including edge cases
        x = random.randint(-100, 100)
        y = random.randint(-10, 10)  # Smaller range for y to increase chance of zero
        
        # Occasionally send zero as divisor to trigger errors
        if random.random() < 0.2:
            y = 0
        
        app.send_task('tasks.tasks.divide', args=[x, y], queue='queue4')
        print(f"Generated 'divide' task to queue4 with args {x}, {y}")
        time.sleep(delay)

if __name__ == '__main__':
    delay = int(os.getenv('TASK_DELAY', 25))
    generate_tasks(delay)