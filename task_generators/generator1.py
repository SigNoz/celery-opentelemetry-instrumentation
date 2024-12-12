import time
import os
from celery import Celery

broker_url = os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')
app = Celery('task_generators', broker=broker_url, backend='rpc://')

def generate_tasks(delay):
    while True:
        app.send_task('tasks.tasks.add', args=[1, 2], queue='queue1')
        print("Generated 'add' task to queue1")
        time.sleep(delay)

if __name__ == '__main__':
    # delay in seconds
    delay = int(os.getenv('TASK_DELAY', 10))
    generate_tasks(delay)