from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    items = ["shafin","ripon"]
    if request.method == "GET":
        return render_template("index.html", item=items)
    else:
        pass # do something else.


