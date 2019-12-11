import webbrowser

webbrowser.open('https://search.naver.com/search.naver?query=치킨')

brands=["bhc","bbq","페리카나","호식이","네네","또래오래"]


for brand in brands:
    webbrowser.open('https://search.naver.com/search.naver?query=' + brand )