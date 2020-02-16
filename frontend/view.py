from flask import Flask, render_template, url_for, flash, redirect, request
#from frontend import app, db, bcrypt
from datetime import datetime
import requests

app = Flask(__name__)
@app.route("/", methods = ['GET'])
def home():
    return render_template("home.html",
                           posts=requests.get("https://hackthevalley.herokuapp.com/").json())

@app.route("/post", methods = ['GET', 'POST'])
def new_post():
    if request.method == "POST":
        content = request.form['content']
        title = request.form['title']
        data = {"content":content,"title":request.form['title']}
        print(data)
        response = requests.post("https://hackthevalley.herokuapp.com/insert",data=data)
        urls = requests.post("https://hackthevalley.herokuapp.com/tweet").json()
        print(response)
        return render_template("videos.html", title = title, content = content, urls=response.json())
    else:
        return render_template("insert.html")

@app.route("/blank")
def blank():
    sentiments = requests.get("https://hackthevalley.herokuapp.com/sentiment").json()
    senti_vals = []
    dates = []
    for entry in sentiments:
        currVal = float(entry[1])
        currDate = entry[0]
        dates.append(currDate)
        senti_vals.append(currVal)

    total = len(dates)
    change = senti_vals[-1] - senti_vals[-2]
    change = round(change, 3)
    average = sum(senti_vals) / len(senti_vals)
    average = str(round(average, 2))
    posts = requests.get("https://hackthevalley.herokuapp.com/").json()
    newest = []
    newest.append(posts[-1])
    newest.append(posts[-2])
    newest.append(posts[-3])

    return render_template("blank.html", posts=newest, sentiment_values = senti_vals, dates = dates, total = total, change = change, average = average)

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

    total = len(dates)
    change = senti_vals[-1]-senti_vals[-2]
    change = round(change, 3)
    average = sum(senti_vals)/len(senti_vals)
    average = str(round(average,2))

    return render_template("analytics.html", sentiment_values = senti_vals, dates = dates, total = total, change = change, average = average)

@app.route("/test")
def test():
    return render_template("test.html", urls=["https://www.youtube.com/embed/MmC4b7gPY0Q","https://www.youtube.com/embed/MmC4b7gPY0Q"])

@app.route("/insert")
def insert():
    return render_template("insert.html")

@app.route("/upload",methods=['GET','POST'])
def upload():
    if request.method == "POST":
        url = request.form['URL']
        print(requests.post("https://hackthevalley.herokuapp.com/photo",data={'url':url}))
        sentiments = requests.get("https://hackthevalley.herokuapp.com/sentiment").json()
        senti_vals = []
        dates = []
        for entry in sentiments:
            currVal = float(entry[1])
            currDate = entry[0]
            dates.append(currDate)
            senti_vals.append(currVal)

        total = len(dates)
        change = senti_vals[-1] - senti_vals[-2]
        change = round(change, 3)
        average = sum(senti_vals) / len(senti_vals)
        average = str(round(average, 2))
        posts = requests.get("https://hackthevalley.herokuapp.com/").json()
        newest = []
        newest.append(posts[-1])
        newest.append(posts[-2])
        newest.append(posts[-3])

        return render_template("blank.html", posts=newest, sentiment_values=senti_vals, dates=dates, total=total,
                               change=change, average=average)

    else:
        return render_template("upload.html")
