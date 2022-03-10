from flask import Flask, request
from flask_cors import CORS
from flask import render_template

app = Flask(__name__, template_folder="./templates")
CORS(app)

message = "Hello world from the flask backend"

@app.route("/")
def test_api():
    global message
    return {"message":message},200

@app.route("/message_post", methods = ["GET", "POST"])
def message_post():
    global message
    if request.method == "GET":
        return render_template("post_message.html")
    form = request.form
    new_message = form.get("message")
    if new_message:
        message = new_message
    return render_template("post_message.html")

app.run(
    host="0.0.0.0",
    port="5000"
)
