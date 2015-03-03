import os
from celery import Celery

app = Celery('tasks')
app.config_from_object("celeryconfig")

@app.task
def add(x, y):
    r = x + y
    print "task arguments: {x}, {y}".format(x=x, y=y)
    print "task result: {r}".format(r=r)
    return r
