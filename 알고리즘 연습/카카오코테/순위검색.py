from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    tmp=[0,1,2,3]
    score_dict=dict()
    for words in info:
        words = words.split()
        for i in range(0,5):
            for position in combinations(tmp,i):
                tmp_words = words[:]
                for k in position:
                    tmp_words[k]="-"
                if tmp_words[0]+tmp_words[1]+tmp_words[2]+tmp_words[3] in score_dict:
                    score_dict[tmp_words[0]+tmp_words[1]+tmp_words[2]+tmp_words[3]].append(int(tmp_words[4]))
                else:
                    score_dict[tmp_words[0]+tmp_words[1]+tmp_words[2]+tmp_words[3]] = [int(tmp_words[4])]
    
    for k in score_dict.keys():
        score_dict[k].sort()

    answer = []
    for quer in query:
        question = quer.split(" ")
        # cnt=0
        if question[0]+question[2]+question[4]+question[6] in score_dict:
            answer.append(len(score_dict[question[0]+question[2]+question[4]+question[6]])-bisect_left(score_dict[question[0]+question[2]+question[4]+question[6]],int(question[-1])))
            
            # for i in score_dict[question[0]+question[2]+question[4]+question[6]]:
            #     if i >= int(question[-1]):
            #         cnt+=1   
            # answer.append(cnt)
        else:
            answer.append(0)
    print(score_dict)
    print(answer)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info,query)

#  bisect 는 이진 탐색해주는거 자동으로 해준다 bisect_left(score_dict[question[0]+question[2]+question[4]+question[6]],int(question[-1]))      1번째는 찾고자하는 배열 2번째는 기준이 되는값 3,4 번째는 시작 끝값 // 찾는 값의 기준위치 왼쪽을 찾아준다. 