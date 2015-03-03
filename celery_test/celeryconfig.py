from datetime import timedelta

BROKER_URL = "redis://redis.local:6379/0"
BROKER_TRANSPORT_OPTIONS = {'fanout_prefix': True, 'fanout_patterns': True, 'visibility_timeout': 480}
CELERY_RESULT_BACKEND = BROKER_URL

CELERYBEAT_SCHEDULE = {
    'addrandom-to-16K-every-2-seconds': {
        'task': 'celery_test.tasks.addrandom', # notice that the complete name is needed
        'schedule': timedelta(seconds=2),
        'args': (16000, 42)
    },
}

CELERY_TIMEZONE = 'UTC'
