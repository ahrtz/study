import requests

#1 요청 보내기 
result = requests.get('https://naver.com').status_code
print(result)
if result ==200 :
    print("접속 성공")
elif result ==404:
    print ("page가 존재하지 않음")