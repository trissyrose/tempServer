from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<div><strong>Hello world</strong></div>"


@app.route("/iphobes")
def iphobes():
    return "hi iphobes <3"
