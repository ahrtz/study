def solution(brown, red):
    tot = brown+red
    len_list=[]
    for i in range(2,tot//2+1):
        if tot%i==0:
            len_list.append((i,int(tot/i)))
    for (l,j) in len_list:
        if 2*(l+j)-4 ==brown:
            if l>=j:
                answer=[l,j]
                break
    
    return answer