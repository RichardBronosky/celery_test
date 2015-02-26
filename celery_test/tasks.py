import os
from celery import Celery

app = Celery('tasks', backend=os.environ['CELERY_RESULT_BACKEND'], broker=os.environ['BROKER_URL'])

@app.task
def add(x, y):
    r = x + y
    print "task arguments: {x}, {y}".format(x=x, y=y)
    print "task result: {r}".format(r=r)
    return r
