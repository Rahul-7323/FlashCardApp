from .workers import celery
from datetime import datetime

@celery.task()
def say_hello(name):
    print("INSIDE THE TASK")
    print(f"Hello {name}!")