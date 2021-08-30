from flask import Flask

app = Flask(__name__)

@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    return f"{num1+num2}"

@app.route('/sub/<float:num1>/<float:num2>')
def sub(num1, num2):
    return f"{num1-num2}"

@app.route('/mult/<float:num1>/<float:num2>')
def mult(num1, num2):
    return f"{num1*num2}"

@app.route('/div/<float:num1>/<float:num2>')
def div(num1, num2):
    if num2 != 0:
        return f"{num1/num2}"
    else:
        return "Division by zero is undefined"

@app.route('/math/<op>/<float:num1>/<float:num2>')
def math(op, num1, num2):
    if op == 'add':
        return f"{num1+num2}"
    elif op == "sub":
        return f"{num1-num2}"
    elif op == "mult":
        return f"{num1*num2}"
    elif op == "div":
        if num2 != 0:
            return f"{num1/num2}"
        else:
            return "Division by zero is undefined"
    else:
        return "Operation not implemented"