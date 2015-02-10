from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://guest@rabbit//')

@app.task
def add(x, y):
    return x + y
