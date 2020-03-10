T=int(input())
for tc in range(T):
    N,M = map(int,input().split())
    N_list  = list(map(int,input().split()))
    M_list = list(map(int,input().split()))
    score = [0]*N
    tmp=0
    for i in M_list:
        for k in range(len(N_list)):
            if i>=N_list[k]:
                score[k]+=1
                break
    
    result = score.index(max(score))
    print("#{} {}".format(tc+1,result+1))



        