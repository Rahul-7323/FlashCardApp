import os
from flask import request, render_template, redirect, url_for, jsonify
from main import app as app
from flask_security import login_required, current_user
from flask_sse import sse
from application import tasks

import requests
import json
from random import shuffle
from math import ceil

from datetime import datetime
import pytz

tz_IND = pytz.timezone('Asia/Kolkata')
count = 0
cards = []
    
@app.route("/say_hello/<name>")
def say_hello(name):
    job = tasks.say_hello.delay(name)
    result = job.wait()
    return str(result), 200

@app.route("/print_current_time")
def print_current_time():
    now = datetime.now()
    print("now in flask = ",now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time = ", dt_string)
    job = tasks.print_current_time.apply_async(countdown = 3)
    result = job.wait()
    return str(result), 200

@app.route('/test_send_message/<id>')
def test_send_message(id):
    sse.publish({"message":"Test SSE message from server"}, type='SSE_TEST', channel=id)
    return 'OK',200

@app.route('/test_show_messages')
def test_show_messages():
    return render_template("sse_show_update.html", error = None)

@app.route('/export_deck/<user_id>/<deck_id>')
def export_deck(user_id,deck_id):
    job = tasks.export_deck.delay(user_id,deck_id)
    return {"job_id":str(job)},200
