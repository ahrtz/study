def solution(m,k):
    answer=""
    answer_idx=[]    
    
    for i in k:
        if answer_idx:
            answer_idx.append(m.index(i,answer_idx[-1]))
        else:
            answer_idx.append(m.index(i))
    for idx in range(len(m)):
        if idx not in answer_idx:
            answer+=m[idx]


    print(answer)
    return answer

m="acbbcdc"
k="abc"
solution(m,k)
