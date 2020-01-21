from flask import Flask,render_template, request
from decouple import config
import requests, pprint
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

    #2 사용자 아이디,메세지 추출
    chat_id1 = request.get_json().get("message").get("chat").get("id")
    message1 = request.get_json().get("message").get("text")

    # 사용자가 로또라고 입력하면 로또번호 6개 돌려주기
    if message1 =="로또":
        message1 = np.random.randint(1,46,6)
        #result = random.sample ((1,46),6)
        requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id1}&text={message1}')
    elif message1[0:3] == "/번 ":
        url_trans = 'https://translation.googleapis.com/language/translate/v2'
        G_key = config('GOOGLE_TOKEN')

        data= {
            "q" : message1[3:],
            'source' : "ko",
            'target' : "en",
            'format' : 'text'
            }
        response =requests.post(f'{url_trans}?key={G_key}',data).json()['data']['translations'][0]["translatedText"]


        requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id1}&text={response}')
    elif message1[0:4] =="/티어 ":

        Riot_key = config('api_key')
        nick =  message1[4:]
        url_r = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{nick}?api_key={Riot_key}"
        res=requests.get(url_r).json()

        # pprint.pprint(res)
        id=res.get('id')
        summonerLevel = res.get('summonerLevel')

        ### 저 아이디를 이용해서 티어 검색
        url1 = f'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={Riot_key}'
        res2 = requests.get(url1).json()

        tier = res2[0].get('tier')
        solo = res2[0].get('queueType')
        rank = res2[0].get('rank')
        points = res2[0].get("leaguePoints")

        response = f"{nick}의 티어는 {tier} {rank} {points}점 {solo} 입니다. "
        requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id1}&text={response}')
    else:


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
