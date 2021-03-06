# If you are using the Windows command prompt, use set instead of export 
# export FLASK_ENV=development
# export FLASK_APP=app.py
# pip freeze > requirements.txt
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# create flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret key"

# create a form class
class NamerForm(FlaskForm):
    name = StringField("What is your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

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
    # return "<h1>Hello {}</h1>".format(name)

# invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# internal server error    
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form submitted succesfully")
    return render_template("name.html", name=name, form=form)



