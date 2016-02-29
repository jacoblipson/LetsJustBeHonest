from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'letsjustbehonest.settings')

app = Celery('letsjustbehonest')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# TODO - follow this guide for running celery via supervisord:
# http://michal.karzynski.pl/blog/2014/05/18/
# setting-up-an-asynchronous-task-queue-for-django-using-celery-redis/

# TODO - modify celery to run a celery beat worker
