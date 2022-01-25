from crypt import methods
from unittest import result
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "你好"

@app.route("/user/<name>")
def welcome(name):
    return "你好%s"%name


@app.route("/user/<int:id>")
def welcome2(id):
    return "你好, %d号会员"%id

@app.route("/index")
def indexPage():
    time = datetime.date.today()
    list = ["f1", "f2", "f3"]
    task = {"t1":"任务1"}
    return render_template("index.html", var = time, vars = list, task=task)

@app.route("/test/register")
def registerPage():
    return render_template("test/register.html")

@app.route("/test/result", methods = ['POST', 'GET'])
def resultPage():
    if request.method == 'POST':
        result = request.form
        return render_template("test/result.html", result=result)
    else: 
        return "1"





if __name__ == "__main__":
    app.run()