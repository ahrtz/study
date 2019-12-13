from flask import Flask, render_template,request
from datetime import datetime
import random
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '접속 완료'
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/mulcam')
def mulcam():
    return '20층에는 밥집이 있습니다.'

@app.route('/dday')
def dday():
    today = datetime.now()
    new_year = datetime(2020,1,1)
    result = new_year - today
    return f'30 까지 {result.days}일 남았습니다'

@app.route('/greeting/<string:name>')
def greeting(name):

    return render_template('greeting.html',html_name = name)
    #f'반갑습니다. {name}님! :'


@app.route('/cube/<int:number>')
def cube(number):
    result = number**3
    return render_template('cube.html',number=number,result=result)
    #return f'{number}의 세제곱 값은 {number**3}입니다'


@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['보쌈 정식','뼈다구 해장국','콩나물 국밥','방어회','치킨스페셜','오마카세']

    order = [random.choice(menu) for i in range(people)]
    #order = random.sample(menu,people)
    return str(order)

#여기꺼는 variable routing : 주소 자체를 변수로 사용하는것을 의미 
# jinja2도 사용 html에서 for 문 사용할때 쓰는 문법임 
@app.route('/movie')
def movie():
    movies = ['나이브스 아웃','조커','엔드게임',"어 웨이 아웃"]
    return render_template('movie.html',movie_list=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html',age=age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/blah')
def blah():
    name = request.args.get('name')
    menu = ['보쌈 정식','뼈다구 해장국','콩나물 국밥','방어회','치킨스페셜','오마카세']
    menu1 = ['떡볶이','매운갈비찜','그냥 갈비찜','회냉면','연어덮밥','한우 오마카세']
    menu2 = ['핫도그','송주불냉면','호미닭발','모듬회','순대국밥','시래기국']
    # sample 사용하면 리스트 형태로들어온다.
    # tmp = random.sample(first_options,1)
    # print(tmp,type(tmp),tmp[0])
    
    #choice 를 사용하면 str 형태로 들어온다
    order1 = random.choice(menu) 
    order2 = random.choice(menu1) 
    order3 = random.choice(menu2) 
    return render_template('blah.html',name=name,order=order1,order1=order2,order2=order3)
# app.py 가장하단에 위치
# 앞으로 flask run 으로 서버를 켜는게 아니라 python app.py로 서버를 실행한다
# 내용이 바뀌어도 서버를 껏다 켜지 않아도 된다.
if __name__== '__main__':
    app.run(debug=True)
