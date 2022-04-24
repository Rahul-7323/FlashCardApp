#!/bin/bash

# Start the flask server using gunicorn
gunicorn main:app --worker-class gevent --bind 0.0.0.0:5000 --workers=4 &

# start the celery workers
celery -A main.celery worker -l info &

# wait for any process to exit
wait -n

# Exit with status of the process that exited first
exit $?