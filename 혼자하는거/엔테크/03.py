from itertools import combinations
def solution(histogram):
    answer =0
    for tmp in combinations(range(len(histogram)),2):
        tmp_hist = histogram[:]
        tmp_ans=0
        al=min(tmp_hist[tmp[0]],tmp_hist[tmp[1]])
        for i in range(tmp[0]+1,tmp[1]):
            tmp_hist[i]=al
            tmp_ans+=al
        # tmp_hist[tmp[0]:tmp[1]]=min(tmp_hist[tmp[0]],tmp_hist[tmp[1]])
        
        # print(tmp_hist)
        if tmp_ans>answer:
            answer=tmp_ans
    return answer

histogram =[6, 5, 7, 3, 4, 2]
answer=0
for tmp in combinations(range(len(histogram)),2):
    tmp_hist = histogram[:]
    tmp_ans=0
    for i in range(tmp[0]+1,tmp[1]):
        tmp_hist[i]=min(tmp_hist[tmp[0]],tmp_hist[tmp[1]])
        tmp_ans+=min(tmp_hist[tmp[0]],tmp_hist[tmp[1]])
    # tmp_hist[tmp[0]:tmp[1]]=min(tmp_hist[tmp[0]],tmp_hist[tmp[1]])
    
    # print(tmp_hist)
    if tmp_ans>answer:
        answer=tmp_ans
print(answer)