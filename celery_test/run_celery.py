import sys
import os
import pwd
from celery.__main__ import main

def abate():
  if(os.getuid() == 0):
    pw = pwd.getpwnam('nobody')
    os.setgid(pw.pw_gid)
    os.setuid(pw.pw_uid)

def worker():
  abate()
  # sudo -u nobody celery -A celery_test worker --loglevel=info
  sys.argv = ['', '-A', 'celery_test', 'worker', '--loglevel=info']
  sys.exit(main())

def beat():
  abate()
  # sudo -u nobody celery -A celery_test worker -B --loglevel=info -s /tmp/celerybeat-schedule
  sys.argv = ['', '-A', 'celery_test', 'worker', '-B', '--loglevel=info', '-s', '/tmp/celerybeat-schedule']
  sys.exit(main())
