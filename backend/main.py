from flask import Flask, request, jsonify
import requests
import datetime
from db_helper import DBHelper
from youtube_query import get_link
from NLP import get_sentiment
app = Flask(__name__)
db = DBHelper()
from youtube_query import detect_text_uri

@app.route('/',methods=['GET'])
def get_posts():
    return jsonify(db.get_posts())

@app.route('/insert/',methods=['GET','POST'])
def insert_post():
    if request.method == "POST":
        print(request.form)
        post = {}
        content = request.form['content']
        post['content'] = request.form['content']
        post['title'] = request.form['title']
        post['sentiment'] = get_sentiment(request.form['title'])
        now = datetime.datetime.now()
        post['date'] = now.strftime("%m/%d/%Y")
        post['post_id'] = db.get_latest_id()
        print(post)
        db.insert_post(post)
        content = content.split(".")
        urls = [get_link(sentence) for sentence in content if sentence is not None]
        return jsonify(urls)

    return jsonify(db.get_posts())


@app.route('/sentiment',methods=['GET'])
def sentiment():
    return jsonify(db.get_sentiment())

@app.route('/photo/<url>',methods=['POST'])
def photo_convert(url):
    post = {}
    post['content'] = detect_text_uri(url)
    post['sentiment'] = get_sentiment(post['content'])
    post['title'] = ""
    post['post_id']= db.get_latest_id()
    now = datetime.datetime.now()
    post['date'] = now.strftime("%m/%d/%Y")
    db.insert_post(post)

    return jsonify(db.get_posts())

if __name__ == "__main__":
    # print(get_sentiment("Hello World"))
    app.run(debug=False)
