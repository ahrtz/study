def sol(k,score):
    temp_score=[]
    # diff = dict()
    temp_idx=[]
    # print(temp_idx)
    for i in range(len(score)-1):
        temp_score.append(score[i]-score[i+1])
    temp = set(temp_score)
    for i in temp:
        if temp_score.count(i)>=k:
            temp_idx+=(list(filter(lambda x: temp_score[x]==i,range(len(temp_score))) ))

    idx_cnt =2 
    temp_idx = sorted(temp_idx)
    for idx in range(1,len(temp_idx)):
        if temp_idx[idx] == temp_idx[idx-1]+1:
            idx_cnt+=1
        else:
            idx_cnt+=2
    if idx_cnt==2:
        idx_cnt=0

    real_answer = len(score)
    print(temp_score)
    print(temp_idx)
    return real_answer-idx_cnt
sol(3,	[1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100])