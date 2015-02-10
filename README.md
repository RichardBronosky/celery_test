An implementation of the celery 'add' example
=============================================

An example that can be found in [The tutorial on celeryproject.org
](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)

Run the worker with:

    sudo -u nobody celery -A celery_test.tasks worker --loglevel=info
