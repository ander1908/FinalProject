from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "key1": "value1",
        "key2": 2
            })