import time
import os
import random
from celery import Celery

broker_url = os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')
app = Celery('task_generators', broker=broker_url, backend='rpc://')

def generate_tasks(delay):
    while True:
        # Generate random numbers including potential overflow cases
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, 1000)
        
        app.send_task('tasks.tasks.multiply', args=[x, y], queue='queue2')
        print(f"Generated 'multiply' task to queue2 with args {x}, {y}")
        time.sleep(delay)

if __name__ == '__main__':
    delay = int(os.getenv('TASK_DELAY', 15))
    generate_tasks(delay)