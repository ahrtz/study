from collections import Counter 
# def solution(genres, plays):
genres =['classic', 'pop', 'classic', 'classic', 'pop']    
plays =[500, 600, 150, 800, 2500]	

# 사전들 초기화
def solution(genres, plays):
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
        
    # 재생 횟수 내림차순으로 장르별로 정렬
    genreSort = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)
    
    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, totalPlay) in genreSort:
        d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))
        print(d)    
        answer += [ idx for (play, idx) in d[genre][:2] ]
    return answer
print(solution(genres,plays))