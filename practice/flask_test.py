from flask import Flask
from datetime import datetime
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask 웹사이트다!'

# 코드를 실행시키고 나오는 http 주소로 이동
@app.route('/backend_sample')
def backend_sample():
    return render_template('backend_sample.html', backend_result = "1000개!!")
app.run()