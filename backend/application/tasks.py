from .workers import celery
from datetime import datetime
from celery.schedules import crontab
from flask_sse import sse
import time

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

@celery.task(bind=True)
def export_deck(self,user_id,deck_id):
    now = datetime.now()
    print("STARTING DECK EXPORT JOB AT",now)
    print("Job id",self.request.id)
    time.sleep(3)
    print("DECK EXPORT JOB COMPLETE")
    message = "Exported the deck {}".format(deck_id)
    sse.publish({"job_id":self.request.id,"message":message}, type='Export', channel=str(user_id))
    return "EXPORT COMPLETED"



