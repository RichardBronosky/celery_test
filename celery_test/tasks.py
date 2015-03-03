import random
from celery import Celery

app = Celery('celery_test') # without this explicit name Celery will list the app as "__main__"

@app.task
def add(x, y):
    r = x + y
    print "task arguments: {x}, {y}".format(x=x, y=y)
    print "task result: {r}".format(r=r)
    return r

@app.task
def addrandom(x, *args): # *args are not used, just there to be interchangable with add(x, y)
    y = random.randint(1,100)
    print "passing to add(x, y)"
    return add(x, y)
