import os
from flask import request, render_template, redirect, url_for, jsonify
from flask import current_app as app
from flask_security import login_required, current_user
import requests
import json
from random import shuffle
from math import ceil

from datetime import datetime
import pytz

tz_IND = pytz.timezone('Asia/Kolkata')
count = 0
cards = []


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'txt'}

def extract_cards():
    try:
        f = open(os.path.join(app.config['UPLOAD_FOLDER'], 'deck_import.txt'),encoding='utf-8')
        content = f.readlines()
        f.close()
        cards = []
        for line in content:
            line = line.strip().split(';')
            cards.append({'front':line[0],'back':line[1]})
        return cards
    except:
        return None

@app.route("/")
def index():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/decks", methods=["GET"])
@login_required
def decks():
    return render_template("decks.html")

@app.route("/manage_decks", methods=["GET"])
@login_required
def manage_decks():
    return render_template("manage_decks.html")

@app.route("/add_decks", methods=["GET", "POST"])
@login_required
def add_decks():
    if request.method == "POST":
        form = request.form
        deck_name = form["deck_name"]
        now = datetime.now(tz=tz_IND)
        date_time = now.strftime("%d %B, %Y, %I:%M:%S %p")
        user_id = current_user.id
        payload = {
            'deck_name':deck_name,
            'user_id':user_id,
            'total_score':0,
            'last_review_time':date_time        
        }
        deck_resp = requests.post('http://127.0.0.1:5000/api/deck',data=payload)
        return jsonify(json.loads(deck_resp.text))
    else:
        return render_template("add_decks.html")

@app.route("/add_cards", methods=["GET", "POST"])
@login_required
def add_cards():
    if request.method == "POST":
        form = request.form
        deck_id = form.get('decklist')
        front = form.get('front')
        back = form.get('back')
        payload = {
            'deck_id':deck_id,
            'front':front,
            'back':back     
        }
        card_resp = requests.post('http://127.0.0.1:5000/api/card',data=payload)
        return jsonify(json.loads(card_resp.text))
    else:
        return render_template("add_cards.html")

@app.route("/decks/cards/<int:deck_id>/<deck_name>")
@login_required
def cards_(deck_id,deck_name):
    resp = requests.get(f"http://127.0.0.1:5000/api/card/deck/{deck_id}")
    cards = json.loads(resp.text)
    return render_template("cards.html",cards = cards,deck_id = deck_id,deck_name=deck_name)

@app.route("/decks/delete_deck/<int:deck_id>")
@login_required
def delete_deck(deck_id):
    requests.delete(f"http://127.0.0.1:5000/api/deck/{deck_id}")
    return redirect(url_for("decks"))

@app.route("/decks/export_deck/<int:deck_id>/<deck_name>")
@login_required
def export_deck(deck_id,deck_name):
    resp = requests.get(f"http://127.0.0.1:5000/api/card/deck/{deck_id}")
    data = [dict(row) for row in json.loads(resp.text)]
    f = open(f'static/files/deck_export.txt','w',encoding='utf-8')
    f.write('front'+';'+'back'+'\n')
    for row in data:
        f.write(row["front"]+";"+row["back"]+'\n')
    f.close()
    return render_template("export_deck.html")

@app.route("/decks/cards/<int:deck_id>/<deck_name>/delete_card/<int:card_id>", methods = ["DELETE"])
@login_required
def delete_card(deck_id,card_id,deck_name):
    resp = requests.delete(f"http://127.0.0.1:5000/api/card/{card_id}")
    return jsonify(json.loads(resp.text))

@app.route("/decks/review/<int:deck_id>/<deck_name>")
@login_required
def review(deck_id,deck_name):
    global count
    global cards
    if request.method == "GET":
        now = datetime.now(tz=tz_IND)
        date_time = now.strftime("%d %B, %Y, %I:%M:%S %p")
        resp = requests.put(f"http://127.0.0.1:5000/api/deck/update_lrt/{deck_id}",data={'last_review_time':date_time})
        resp = requests.get(f"http://127.0.0.1:5000/api/card/deck/{deck_id}")
        cards = json.loads(resp.text)
        shuffle(cards)
        count = 0
        if len(cards) == 0:
            card = None
        else:
            card = cards[count]
        count+=1
        return render_template("review.html",card = card,deck_id = deck_id)

@app.route("/deck/<int:deck_id>/card/<int:card_id>/difficulty/<difficulty>")
@login_required
def review_card(card_id,difficulty,deck_id):
    global cards
    global count
    if difficulty not in ['easy','medium','hard']:
        difficulty = None
    requests.put(f"http://127.0.0.1:5000/api/card/update_difficulty/{card_id}",data={'difficulty':difficulty})
    if count < len(cards):
        card = cards[count]
        count+=1
        return render_template("review.html",card = card,deck_id = deck_id)
    else:
        resp = requests.get(f"http://127.0.0.1:5000/api/card/deck/{deck_id}")
        cards = json.loads(resp.text)
        total_score = 0
        for card in cards:
            if card['difficulty'] == 'easy':
                total_score+=3
            elif card['difficulty'] == 'medium':
                total_score+=2
            elif card['difficulty'] == 'hard':
                total_score+=1
            else:
                total_score+=0
        total_score = ceil(((total_score)/(3*len(cards)))*100)
        requests.put(f"http://127.0.0.1:5000/api/deck/update_ts/{deck_id}",data={'total_score':total_score})        
        return redirect(url_for('decks'))

@app.route("/delete_user",methods = ["GET"])
@login_required
def delete_user():
    user_id = current_user.id
    requests.delete(f"http://127.0.0.1:5000/api/user/{user_id}")
    return redirect(url_for('home'))

@app.route("/import_deck", methods = ["GET","POST"])
@login_required
def import_deck():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(url_for('import_deck'))
        file = request.files['file']
        if file.filename == '':
            return redirect(url_for('import_deck'))
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'deck_import.txt'))
            form = request.form
            deck_id = form.get('decklist')
            cards = extract_cards()
            if cards is not None:
                for card in cards:
                    payload = {
                        'deck_id':deck_id,
                        'front':card['front'],
                        'back':card['back']     
                    }
                    requests.post('http://127.0.0.1:5000/api/card',data=payload)
            return redirect(url_for('decks'))
    else:
        return render_template("import_deck.html")