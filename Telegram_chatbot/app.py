from flask import Flask,render_template, request
from decouple import config
import requests,pprint,random
import numpy as np


app = Flask(__name__)

url='https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chai_id = config('CHAT_ID')




@app.route('/')
def hello_world():
    return 'Hello, World!'

# 웹 훅을 걸어야 댄다
@app.route(f'/{token}',methods=['POST'])
def telegram():
    #1 텔레그램이 보내주는 데이터 구조확인
    pprint.pprint(request.get_json())
    #2 사용자 아이디,메세지 추출
    chat_id1 = request.get_json().get("message").get("chat").get("id")
    message1 = request.get_json().get("message").get("text")
    
    # 사용자가 로또라고 입력하면 로또번호 6개 돌려주기
    if message1 =="로또":
        message1 = np.random.randint(1,46,6)
        #result = random.sample ((1,46),6)
    
    elif message1[0:4] == "/번역 ":
        url_trans = 'https://translation.googleapis.com/language/translate/v2'
        G_key = config('GOOGLE_TOKEN')
        
        data= {
            "q" : message1[4:],
            'source' : "ko",
            'target' : "en",
            'format' : 'text'
            }
        response =requests.post(f'{url_trans}?key={G_key}',data).json()['data']['translations'][0]["translatedText"]

        
        requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id1}&text={response}')
    else:
        result = message1
    
    #3 텔레그램 API에 요청해서 답장 보내주기
        requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id1}&text={message1}')
    
    return '',200







@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    message = request.args.get('message') # 데이터를 추출 flask 내부

    requests.get(f'{url}/bot{token}/sendMessage?chat_id={chai_id}&text={message}')
    # 텔레그램 api로 메세지 보내기 이 리퀘스츠는 보내는건가 
    return "메세지 전송 완료"

# 이 부분은 반드시 파일 최하단에 위치해야 한다 
# 자동 으로 업데이트
if __name__ == '__main__':
    app.run(debug=True)