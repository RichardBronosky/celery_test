from sys import argv
from celery_test.tasks import add
from celery.exceptions import TimeoutError

def main():
    val = [32, 16] # default values to use in case non-integers are passed
    for i in range(2):
        try:
            val[i] = int(argv[i+1])
        except (ValueError,IndexError):
            pass
    res = add.delay(*val)
    try:
        res.get(timeout=2)
    except (TimeoutError,):
        print "The task made it to the queue, but no result was given."
        print "Perhaps there are no workers or they are all busy"
    else:
        print "{val0} + {val1} = {out}".format(val0=val[0], val1=val[1], out=res.result)
