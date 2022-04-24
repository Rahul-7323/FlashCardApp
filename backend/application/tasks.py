from .workers import celery
from datetime import datetime
from celery.schedules import crontab
from flask_sse import sse
from flask import url_for
from main import app as app
from .database import db
from .models import User,Deck
import os
import time
import requests

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, print_current_time.s(), name = 'at every 10 seconds')
    sender.add_periodic_task(120.0, cleanup_exports.s(), name = 'remove all the export files')
    sender.add_periodic_task(10.0, daily_remainder.s(), name = 'Send message to discord to revise daily')
    #sender.add_periodic_task(crontab(hour=21, minute=15), daily_remainder.s(), name = 'Send daily reminders in discord to revise')

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
    deck = Deck.query.filter(Deck.deck_id == deck_id).scalar()
    print(deck.deck_name)
    f = open(f'static/files/{self.request.id}.txt','w',encoding='utf-8')
    for card in deck.cards:
        f.write(card.front+','+card.back+'\n')
    f.close()
    time.sleep(4)
    print("DECK EXPORT JOB COMPLETE")
    message = "Exported the deck {}".format(deck_id)
    export_url = 'http://localhost:5000/static/files/{}.txt'.format(self.request.id)
    sse.publish({"job_id":self.request.id,"message":message,"url":export_url}, type='Export', channel=str(user_id))
    return "EXPORT COMPLETED"

@celery.task(bind=True)
def cleanup_exports(self):
    try:
        files = os.listdir('static/files')
        for file in files:
            os.remove(f'static/files/{file}')
    except:
        pass

@celery.task(bind=True)
def daily_remainder(self):
    users = User.query.all()
    for user in users:
        url = user.webhook_url
        payload = {
            "username": "FlashCardApp Bot",
            "avatar_url": "https://gravatar.com/avatar/6a4bebbfceea7807eb0758fb32510a64?s=400&d=robohash&r=x",
            "embeds": [
                {
                    "title": "Revise Today!",
                    "description": "Revising daily keeps your mind sharp. Don't forget to revise today.",
                    "color": 15258703
                }
            ]
        }
        try:
            response = requests.request("POST",url,json=payload)
            print(response.text)
        except:
            pass

@celery.task(bind=True)
def webhook_test(self,user_id):
    user = User.query.filter(User.id == user_id).scalar()
    url = user.webhook_url
    payload = {
        "username": "FlashCardApp Bot",
        "avatar_url": "https://gravatar.com/avatar/6a4bebbfceea7807eb0758fb32510a64?s=400&d=robohash&r=x",
        "embeds": [
            {
                "title": "Title",
                "description": "Text message. You can use Markdown here. *Italic* **bold** __underline__ ~~strikeout~~ [hyperlink](https://google.com) `code`",
                "color": 15258703
            }
        ]
    }
    try:
        response = requests.request("POST",url,json=payload)
        print(response.text)
    except:
        pass
