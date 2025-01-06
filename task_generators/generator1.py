import time
import os
import random
from celery import Celery

broker_url = os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')
app = Celery('task_generators', broker=broker_url, backend='rpc://')

def generate_tasks(delay):
    while True:
        # Generate random numbers including edge cases
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        
        app.send_task('tasks.tasks.add', args=[x, y], queue='queue1')
        print(f"Generated 'add' task to queue1 with args {x}, {y}")
        time.sleep(delay)

if __name__ == '__main__':
    delay = int(os.getenv('TASK_DELAY', 10))
    generate_tasks(delay)