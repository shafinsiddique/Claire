from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    names = ["shafin","ripon"]
    if request.method == "GET":
        return render_template("index.html", items=names)
    else:
        pass # do something else.


