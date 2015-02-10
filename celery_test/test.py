from celery_test.tasks import add

def main():
    res = add.delay(4, 4)
    res.get(timeout=1)
    print "result: {out}".format(out=res.result)
