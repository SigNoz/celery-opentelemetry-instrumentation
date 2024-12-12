import time
import os
from celery import Celery

broker_url = os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')
app = Celery('task_generators', broker=broker_url, backend='rpc://')

def generate_tasks(delay):
    while True:
        app.send_task('tasks.tasks.multiply', args=[3, 4], queue='queue2')
        print("Generated 'multiply' task to queue2")
        time.sleep(delay)

if __name__ == '__main__':
    delay = int(os.getenv('TASK_DELAY', 15))
    generate_tasks(delay)