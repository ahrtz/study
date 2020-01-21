import requests
from decouple import config



url='https://api.telegram.org'

token = config('TELEGRAM_BOT_TOKEN')

chai_id = config('CHAT_ID')
#chai_id = '996522501' 민주 아디 실험용
#chat_id = requests.get(f'{url}/bot{token}/getUpdates').json()["result"][0]['message']["from"]["id"]


text = input("메세지를 입력하세요 :")

send_message = requests.get(f'{url}/bot{token}/sendMessage?chat_id={chai_id}&text={text}')

#print(chat_id)