
from flask import Flask, render_template, request, redirect, url_for
import joblib
import csv
import pandas as pd
import numpy as np
#import joblib

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
    df = pd.read_csv('teams.csv')
    df = df[df['Name'] == f'{usr}']
    df.drop('Name', axis=1, inplace=True)
    clean_team = np.array(df.iloc[0]).reshape(1,-1)
    loaded_model_svm=joblib.load('SVM.sav')
    result = loaded_model_svm.predict(clean_team)

    win_lose_dict = {
        0: 'are not',
        1: 'are'
    }
    txt_result = win_lose_dict[result[0]]
    
    return f"<h1>The {usr}s {txt_result} going to make the playoffs</h1>"
    # csvreader = csv.reader("teams.csv")
    # next(csvreader,None)
    # for row in csvreader:
    #     if row[0] == usr:
    #         #grab row assign to array
    #         team = row
    #         cleaned_team = team.pop(0)
    #         #apply model
            
    #         filename = 'SVM.sav'
    #         loaded_model=joblib.load(filename)
    #         result=loaded_model(cleaned_team)
    #         if result[0] == 0:
    #             status = " are not "
    #         else:
    #             status = " are "    
    #         return f"<h1>The {usr}s {status}going to make the playoffs</h1>"
               
            
    
    

if __name__ == '__main__':
    app.run(debug=True)