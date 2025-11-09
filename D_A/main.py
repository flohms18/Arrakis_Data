from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Lisan Al Gaïb</h1>"

@app.route('/arrakis')
def planet():
    return "<h1>Arrakis page</h1>"
