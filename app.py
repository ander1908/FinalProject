
from flask import Flask, render_template, request, redirect, url_for

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.ext.declarative import declarative_base
import csv
import joblib

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST","GET"])
def search():
    if request.method =="POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:    
        return render_template("search.html")

@app.route("/<usr>")
def user(usr):
    csvreader = csv.reader("teams.csv")
    next(csvreader,None)
    for row in csvreader:
        if row[0] == usr:
            #grab row assign to array
            team = row
            cleaned_team = team.pop(0)
            #apply model
            
            filename = 'SVM.sav'
            loaded_model=joblib.load(filename)
            result=loaded_model(cleaned_team)
            if result[0] == 0:
                status = " are not "
            else:
                status = " are "    
            return f"<h1>The {usr}s {status}going to make the playoffs</h1>"
               
            
    
    

if __name__ == '__main__':
    app.run(debug=True)