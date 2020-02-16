from flask import Flask, request, jsonify
import requests
from NLP import get_sentiment
from db_helper import DBHelper
app = Flask(__name__)
db = DBHelper()

@app.route('/',methods=['GET'])
def get_posts():
    return jsonify(db.get_posts())

@app.route('/insert',methods=['POST'])
def insert_post():
    post = (request.form['post']).to_dict()
    post['sentiment'] = get_sentiment(post['text'])
    db.insert_post(post)
    return jsonify(db.get_posts())

@app.route('/sentiment',methods=['GET'])
def get_sentiment():
    return jsonify(db.get_sentiments())









