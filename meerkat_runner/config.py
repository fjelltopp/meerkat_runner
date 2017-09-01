"""
Celery config file
"""
import os
sentry_dns = os.environ.get('SENTRY_DNS', '')
db_dump = os.environ.get('DB_DUMP', '')


BROKER_URL = 'amqp://guest@dev_rabbit_1//'
CELERY_RESULT_BACKEND = 'rpc://guest@dev_rabbit_1//'

new_url = os.environ.get("MEERKAT_BROKER_URL")
if new_url:
    BROKER_URL = new_url
    CELERY_RESULT_BACKEND = new_url

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_IMPORTS = ('meerkat_abacus.tasks', 'api_background.export_data')
CELERY_ENABLE_UTC = True
#CELERYD_MAX_TASKS_PER_CHILD = 1  # To help with memory constraints
