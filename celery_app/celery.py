from celery import Celery
import os

broker_url = os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')

app = Celery('myproject',
             broker=broker_url,
             backend='rpc://',
             include=['tasks.tasks'])

app.conf.task_queues = {
    'queue1': {
        'exchange': 'queue1',
        'routing_key': 'queue1',
    },
    'queue2': {
        'exchange': 'queue2',
        'routing_key': 'queue2',
    },
    'queue3': {
        'exchange': 'queue3',
        'routing_key': 'queue3',
    },
    'queue4': {
        'exchange': 'queue4',
        'routing_key': 'queue4',
    },
}

app.conf.task_default_queue = 'queue1'

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()