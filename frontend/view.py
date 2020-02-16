from flask import Flask, render_template, url_for, flash, redirect, request
#from frontend import app, db, bcrypt
from datetime import datetime
import requests

app = Flask(__name__)
@app.route("/", methods = ['GET'])
def home():
    return render_template("home.html",
                           posts=requests.get("https://hackthevalley.herokuapp.com/").json())

@app.route("/post/new", methods = ['GET', 'POST'])
def new_post():
    if request.method == "POST":
        content = request.form['content']
        data = {"content":content,"title":request.form['title']}
        print(data)
        response = requests.post("https://hackthevalley.herokuapp.com/insert",data=data)
        print(response)
        return render_template("home.html",posts=requests.get("https://hackthevalley.herokuapp.com/").json())
    else:
        return render_template("insert.html")

@app.route("/analytics")
def analytics():
    sentiments = requests.get("https://hackthevalley.herokuapp.com/sentiment").json()
    senti_vals = []
    dates = []
    for entry in sentiments:
        currVal = float(entry[1])
        currDate = entry[0]
        dates.append(currDate)
        senti_vals.append(currVal)

    return render_template("analytics.html", sentiment_values = senti_vals, dates = dates)

