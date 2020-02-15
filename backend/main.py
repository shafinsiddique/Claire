from flask import Flask
import requests
app = Flask(__name__)
@app.route('/get_posts',methods=['GET'])

def posts():
    return {"message":"success"}





