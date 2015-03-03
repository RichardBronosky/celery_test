from tasks import app

"""
Celery fails to find the file when you pass "celeryconfig" as a string.
To get around this we manually import it because python doesn't have a
a problem with the relative path. Then pass it in as an object.
"""
import celeryconfig

"""
Leaving tasks unconfigured is a pattern that allow it to be extended
later. In this example we assume that the package with be used as the
app for Celery and only apply the coniguration in the __init__.
"""
app.config_from_object(celeryconfig)
