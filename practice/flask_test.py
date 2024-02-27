from flask import Flask
from datetime import datetime
from flask import render_template
from flask import request
import requests 

app = Flask(__name__)

test_name = "pagongble"
test_pw = "pagongble123"
test_coin_count = 10000

@app.route('/')
def index():
     return 'Flask 웹사이트다!'

@app.route('/login', methods=['GET', 'POST'])
def login():   
    if request.method=='POST':
        print("login 버튼을 누름")
        input_value = request.form.to_dict(flat=False)
        print(input_value)
        if (input_value['wallet_id'][0] == test_name) & (input_value['password'][0] == test_pw) :
            return "로그인성공!!!!!!"
        else:
            return render_template('login.html')
        
    return render_template('login.html')

app.run()