from PIL import Image
from flask import Flask, render_template, url_for, flash, redirect, request, app
#from frontend import app, db, bcrypt
#from models import User, Post
from datetime import datetime


app = Flask(__name__)
@app.route('/')

@app.route("/home", methods = ['GET'])
def home():

    entries = [
    {'title': 'First Entry',
    'content': 'This is the content',
    'date': 'January 20, 2020'},
    {'title': 'Second Entry',
    'content': 'This is the content',
    'date': 'January 23, 2020'},
    ]
    return render_template("home.html", posts=entries)

@app.route("/post/new", methods = ['GET', 'POST'])
def new_post():
    # post=Post(title=form.title.data, content = form.content.data, date = datetime.now())
    return render_template("create_post.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

 @app.route('/post/<post_id>')
# def post(post_id):
#     post = Post.query.get_or_404(post_id)
#     return render_template("post.html", title=post.title, post=post)

#routes,form for post

#git add *
#git commit /m "sdfsadfasdf"
#git push

#git pull
