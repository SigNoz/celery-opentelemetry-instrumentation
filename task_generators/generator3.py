import time
import os
from celery import Celery

broker_url = os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')
app = Celery('task_generators', broker=broker_url, backend='rpc://')

def generate_tasks(delay):
    while True:
        app.send_task('tasks.tasks.subtract', args=[5, 3], queue='queue3')
        print("Generated 'subtract' task to queue3")
        time.sleep(delay)

if __name__ == '__main__':
    delay = int(os.getenv('TASK_DELAY', 20))
    generate_tasks(delay)