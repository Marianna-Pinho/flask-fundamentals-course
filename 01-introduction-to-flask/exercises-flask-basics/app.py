from flask import Flask


app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/home')
def welcomeHome():
    return 'welcome home'

@app.route('/welcome/back')
def welcomeBack():
    return 'welcome back'

#This will throw an error, since the return type must be 
# a string, dict, tuple, Response instance, or WSGI callable
@app.route('/sum')
def sum55():
    sum = 5+5
    return sum