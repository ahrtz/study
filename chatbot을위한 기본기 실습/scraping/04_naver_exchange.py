import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/marketindex/"


html = requests.get(url).text



soup = BeautifulSoup(html,'html.parser')




exchange_rate = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").text
print(exchange_rate)