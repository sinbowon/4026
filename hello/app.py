from func import ck_idpw
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/join' , methods=['GET','POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        fname = request.form['fname']
        lname = request.form['lname']
        print(fname,lname)
        if ck_idpw(fname,lname):
            return "로그인성공"
        else:
            return "실패"


@app.route('/')
def index():   #대문 제일 처음
    return '메인페이지'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellovar(name):
    return 'Hello, {}'.format(name)

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return "도라에몽"
    elif num == 2:
        return "진구"
    else:
        return "아잇"



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        print (id,type('id'))
        print (pw,type('pw'))
        # 아이디와 비번이 임의로 정한 값이랑 비교해서 맞으면 맞다 틀리면 틀리다
        if id == 'abc' and pw == '1234':
            return "안녕하세요~{} 님".format(id)
        else:
            return "아이디 또는 패스워드를 확인하세요"

@app.route('/form')
def form():
    return render_template('Test.html')

@app.route('/method', methods=['GET','POST']) 
def method():
    if request.method == 'GET':
        return 'GET으로 전송이다.'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num,name)
        return 'POST이다.학번은: {} 이름은: {}'.format(num,name)


@app.route('/naver')
def naver():
    return redirect("https://www.naver.com/")
    # return render_template("naver.html")
    
    
@app.route('/kakao')
def daum():
    return redirect("https://www.daum.net/")

@app.route('/urltest')
def url_test():
    return redirect(url_for('daum'))

@app.route('/move/<site>')
def move_site(site):
    if site == 'naver':
        return redirect(url_for('naver'))
    elif site == 'daum':
        return redirect(url_for('daum'))
    else:
        return '없는 페이지입니다.'

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL을 확인 하세요", 404  

if __name__ == '__main__':
    with app.test_request_context():  #kakao 로 하든 daum으로 하든 이름변경가능
        print(url_for('daum'))   #함수 def daum():
    app.run(debug=True)  # 소스 수정하면 자동

