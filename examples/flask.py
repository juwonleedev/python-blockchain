from flask import Flask 
from datetime import datetime
from flask import render_template

from flask import requests # APi library

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask 웹사이트다!'

@app.route('/html_sample')
def html_sample():
    return render_template('sample.html')

@app.route('naver')
def naver():
    return render_template('naver.html')

@app.route('/backend_sample')
def backend_sample():
    num_of_coin = 3+6+100
    return render_template('backend_sample.html', backend_result = num_of_coin)

@app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("login 버튼을 누름")
        input_value = request.form.to_dict(flat=False)
        print(input_value)
    return render_template('login.html') # API
app.run()