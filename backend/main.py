from flask import Flask, request, jsonify
import requests
import datetime
from db_helper import DBHelper
from NLP import get_sentiment
app = Flask(__name__)
db = DBHelper()

@app.route('/',methods=['GET'])
def get_posts():
    return jsonify(db.get_posts())

@app.route('/insert/',methods=['GET','POST'])
def insert_post():
    if request.method == "POST":
        print(request.form)
        post = {}
        post['content'] = request.form['content']
        post['title'] = request.form['title']
        post['sentiment'] = get_sentiment(request.form['title'])
        post['date'] = datetime.datetime.now()
        post['post_id'] = db.get_latest_id()
        print(post)
        db.insert_post(post)
    return jsonify(db.get_posts())

@app.route('/sentiment',methods=['GET'])
def sentiment():
    return jsonify(db.get_sentiment())


if __name__ == "__main__":
    # print(get_sentiment("Hello World"))
    app.run(debug=False)



