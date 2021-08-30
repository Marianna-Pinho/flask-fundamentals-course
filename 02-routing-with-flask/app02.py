#This code is not mine. 
#It was copied from: https://www.rithmschool.com/courses/flask-fundamentals/routing-with-flask

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome!"

#let's make up a parameter called name. Its value is going to be WHATEVER someone requests, but we will respond with the string "The name is" along with the value in the URL.
@app.route('/name/<person>')
def say_name(person):
    return f"The name is {person}"

# since all URL parameters are strings, we can convert them right away to another data type in our route definition
@app.route('/name/<int:num>')
def favorite_number(num):
    return f"Your favorite number is {num}, which is half of {num * 2}"