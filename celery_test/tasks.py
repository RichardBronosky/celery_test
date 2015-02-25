import os
from celery import Celery

app = Celery('tasks', backend=os.environ['CELERY_RESULT_BACKEND'], broker=os.environ['BROKER_URL'])

@app.task
def add(x, y):
    return x + y
