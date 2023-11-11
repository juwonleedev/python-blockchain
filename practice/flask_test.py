from flask import Flask
from datetime import datetime
from flask import render_template
from flask import request #서버와 데이터를 주고받는 flask 코드

app = Flask(__name__)

test_id = "Python"
test_pw = "Blockchain"

@app.route('/')
def index():
    return 'Flask 웹사이트다!'

# 코드를 실행시키고 나오는 http 주소로 이동
@app.route('/backend_sample')
def backend_sample():
    return render_template('backend_sample.html', backend_result = "1000개!!")

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        print("login 버튼을 누름")
    input_value = request.form.to_dict(flat=False)
    print(input_value)
    if (input_value['wallet_id'][0] == test_id) & (input_value['password'][0]==test_pw):
        print("로그인 성공")
        return "로그인 성공!!!"
    else:
        return render_template('login.html')
    return render_template('login.html')

app.run()