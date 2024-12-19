# celery_config.py - Using Dedicated Queues for Each Task Type

from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

celery_app.conf.task_queues = (
    Queue('fetch_queue', routing_key='fetch.#'),
    Queue('extract_queue', routing_key='extract.#'),
    Queue('compare_queue', routing_key='compare.#'),
)

celery_app.conf.task_routes = {
    'tasks.fetch_documents_task': {'queue': 'fetch_queue', 'routing_key': 'fetch.documents'},
    'tasks.extract_data_task': {'queue': 'extract_queue', 'routing_key': 'extract.data'},
    'tasks.compare_data_task': {'queue': 'compare_queue', 'routing_key': 'compare.data'},
}

# Starting Workers for Specific Queues
# celery -A celery_config worker --loglevel=info --concurrency=4 -Q fetch_queue
# celery -A celery_config worker --loglevel=info --concurrency=8 -Q extract_queue
# celery -A celery_config worker --loglevel=info --concurrency=2 -Q compare_queue
