from sys import argv
from celery_test.tasks import add

def main():
    val = [4, 4]
    for i in range(2):
        try:
            val[i] = int(argv[i+1])
        except (ValueError,IndexError):
            pass
    res = add.delay(*val)
    res.get(timeout=1)
    print "{val0} + {val1} = {out}".format(val0=val[0], val1=val[1], out=res.result)
