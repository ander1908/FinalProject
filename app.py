from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return {
        "key 1": "value1",
        "key2": 2
            }