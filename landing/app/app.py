from flask import Flask, render_template, request, flash, redirect, url_for, redirect

import webbrowser
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

def add(n1, n2):
    api_url = "http://host.docker.internal:5051/" + str(n1) + "/" + str(n2)
    response = requests.get(api_url)
    result = response.json()['result']
    return result
    #webbrowser.open(api_url, new=2)

def minus(n1, n2):
    api_url = "http://host.docker.internal:5052/" + str(n1) + "/" + str(n2)
    response = requests.get(api_url)
    result = response.json()['result']
    return result

def multiply(n1, n2):
    api_url = "http://host.docker.internal:5053/" + str(n1) + "/" + str(n2)
    response = requests.get(api_url)
    result = response.json()['result']
    return result

def divide(n1, n2):
    api_url = "http://host.docker.internal:5054/" + str(n1) + "/" + str(n2)
    response = requests.get(api_url)
    result = response.json()['result']
    return result

def gcd(n1, n2):
    api_url = "http://host.docker.internal:5055/" + str(n1) + "/" + str(n2)
    response = requests.get(api_url)
    result = response.json()['result']
    return result

def lcm(n1, n2):
    api_url = "http://host.docker.internal:5056/" + str(n1) + "/" + str(n2)
    response = requests.get(api_url)
    result = response.json()['result']
    return result
    
def exponent(n1, n2):
    api_url = "http://host.docker.internal:5057/" + str(n1) + "/" + str(n2)
    response = requests.get(api_url)
    result = response.json()['result']
    return result
    
@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get('first')
    number_2 = request.form.get('second')
    try:
        number_1 = float(number_1)
    except (ValueError, TypeError) as e:
        flash(f'The first number \"{number_1}\" is not a valid number. ')
        number_1 = 0.0
    try:
        number_2 = float(number_2)
    except (ValueError, TypeError) as e:
        flash(f'The second number \"{number_2}\" is not a valid number. ')
        number_2 = 0.0
    operation = request.form.get('operation')
    result = 0.0
    if operation == 'add':
        result = add(number_1, number_2)
    elif operation == 'minus':
        result =  minus(number_1, number_2)
    elif operation == 'multiply':
        result = multiply(number_1, number_2)
    elif operation == 'divide':
        result = divide(number_1, number_2)
    elif operation == 'gcd':
        number_1 = round(number_1)
        number_2 = round(number_2)
        result = gcd(number_1, number_2)
    elif operation == 'lcm':
        number_1 = round(number_1)
        number_2 = round(number_2)
        result = lcm(number_1, number_2)
    elif operation == 'exponent':
        result = exponent(number_1, number_2)
    
    try:
        result = round(result, 2)
    except TypeError as e:
        pass
    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )