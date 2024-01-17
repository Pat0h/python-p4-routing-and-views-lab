#!/usr/bin/env python3
from flask import Flask, render_template_string


app = Flask(__name__)


@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return render_template_string('<h1>{{ title }}</h1>', title=title)

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print the string to the console
    return f"<p>Printed: {param}</p>"

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param + 1))
    return f"<pre>{numbers}</pre>"

@app.route('/math/<float:num1><string:operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2

    return f"<p>Result of {num1} {operation} {num2} is: {result}</p>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
