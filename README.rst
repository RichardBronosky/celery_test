An implementation of the celery 'add' example
=============================================

An example that can be found in `The tutorial on
celeryproject.org <http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html>`__

Run the worker with:

::

    sudo -u nobody celery -A celery_test.tasks worker --loglevel=info

Assumes:

::

    # for rabbit as a backend:
    export CELERY_RESULT_BACKEND='amqp'
    export BROKER_URL='amqp://guest@rabbit.local//'

    # for redis as a backend:
    export CELERY_RESULT_BACKEND='redis://redis.local:6379/0'
    export BROKER_URL='redis://redis.local:6379/0'
