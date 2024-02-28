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

<<<<<<< HEAD
@app.route('/login', methods=['GET', 'POST'])
def login():   
=======
# 코드를 실행시키고 나오는 http 주소로 이동
@app.route('/backend_sample')
def backend_sample():
    return render_template('backend_sample.html', backend_result = "1000개!!")

@app.route('/login',methods=['GET', 'POST']) # API
def login():
>>>>>>> 5ef4248 (Added API comment)
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