from collections import Counter
def solution(N, stages):
    answer = []
    tmp_stage = Counter(stages)
    i=1
    failure_rate=dict()
    mother = 0
    for j in range(1,N+2):
        for k in range(j,N+2):
            mother+=tmp_stage[k]
        if mother == 0:
            failure_rate[j]=0
        else:
            failure_rate[j]=tmp_stage[j]/mother
        mother=0
    a=sorted(failure_rate.items(),key=(lambda x:x[1]),reverse=True)
    for idx in range(len(a)):
        if a[idx][0]==N+1:
            continue
        else:
            answer.append(a[idx][0])

    return answer


N=5
stages=	[2, 1, 2, 6, 2, 4, 3, 3]
    # while i<N+1:
    #     tmp_count= stages.count(i)
    #     mother=0
    #     # print(i)
    #     # print(tmp_count)
    #     for k in range(i,N+2):
    #         mother+= stages.count(k)
    #     # print(i,mother)
    #     if mother==0:
    #         failure_rate[i]=0    
    #     else:
    #         failure_rate[i]=(tmp_count/mother)
    #     # for k in range(tmp_count):
    #     #     stages.remove(i)
        
    #     i+=1
    # res=sorted(failure_rate.items(),key=(lambda x:x[1]),reverse=True)
    # # print(res)
    # for i in range(len(res)):
    #     answer.append(res[i][0])
print(solution(N,stages))