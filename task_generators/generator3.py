import time
import os
import random
from celery import Celery

broker_url = os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')
app = Celery('task_generators', broker=broker_url, backend='rpc://')

def generate_tasks(delay):
    while True:
        # Generate random numbers
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)
        
        app.send_task('tasks.tasks.subtract', args=[x, y], queue='queue3')
        print(f"Generated 'subtract' task to queue3 with args {x}, {y}")
        time.sleep(delay)

if __name__ == '__main__':
    delay = int(os.getenv('TASK_DELAY', 20))
    generate_tasks(delay)