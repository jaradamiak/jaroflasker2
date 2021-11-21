# If you are using the Windows command prompt, use set instead of export 
# export FLASK_ENV=development
# export FLASK_APP=app.py
# pip freeze > requirements.txt
from flask import Flask, render_template
from flask_wtf import Form

# create flask instance
app = Flask(__name__)

# create route
@app.route('/')
@app.route('/index')
def index():
    name = "Janet"
    surname = "Cox"
    myList = ['one', 'dos', 3]
    # return "<h1>Hello world ##!!!</h1>"
    return render_template('index.html', first_name=name, sur_name=surname, list=myList)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)
    return "<h1>Hello {}</h1>".format(name)

