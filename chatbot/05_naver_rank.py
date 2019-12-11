import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://naver.com"


html = requests.get(url).text



soup = BeautifulSoup(html,'html.parser')


# for i in range(1,11):
#     naver_rank = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child("+str(i)+") > a > span.ah_k").text
#     print(naver_rank)

names=soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k")
now = datetime.now()
print(f'{now} 기준 실시간 검색어')

for name in names:
    print(name.text)

    # pip install -r requirements.txt