from collections import Counter 
# def solution(genres, plays):
genres =['classic', 'pop', 'classic', 'classic', 'pop']    
plays =[500, 600, 150, 800, 2500]	
answer = []
# { 장르 : 총 재생 횟수 } 사전
playsDict = {}
# { 장르 : [ ( 플레이 횟수, 고유 번호 ) ] }
d = { }

# 사전들 초기화
for i in range(len(genres)):
    genre = genres[i]
    play = plays[i]
    playsDict[genre] = playsDict.get(genre, 0) + play
    d[genre] = d.get(genre, []) + [ (play, i) ]
# print(playsDict)
# print(d)
genreSort = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)
print(genreSort)