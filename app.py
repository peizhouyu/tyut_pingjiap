from flask import Flask
from flask import render_template
from flask import request
from httpUtil import getCode
from httpUtil import doLogin
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return '2222'
    elif request.method == 'POST':
        number = request.form['number']
        password = request.form['password']
        checkimg = request.form['checkimg']
        #调用登录方法
        doLogin(number,password,checkimg)
        return u'<script>alert("评教完成,为保证无误请登录教务系统查看，如果失败，尝试重新提交(也可以找我反馈");window.close();</script>'

@app.route('/getCheckImg')
def getCheckImg():
    return getCode()

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')