from .workers import celery
from datetime import datetime
from celery.schedules import crontab

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, print_current_time.s(), name = 'at every 10 seconds')

@celery.task()
def say_hello(name):
    print("INSIDE THE TASK")
    return "Hello {}!".format(name)

@celery.task()
def print_current_time():
    print("START")
    now = datetime.now()
    print("now in task = ",now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time = ", dt_string)
    print("COMPLETE")
    return dt_string