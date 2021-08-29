#This code is not mine. 
#It was copied from: https://www.rithmschool.com/courses/flask-fundamentals/introduction-to-flask


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/name')
def welcome():
    return "Welcome to our application!"