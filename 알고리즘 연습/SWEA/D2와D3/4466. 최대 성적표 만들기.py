T=int(input())

for tc in range(T):
    N,K = map(int,input().split())
    score_list=list(map(int,input().split()))
    score_list=sorted(score_list,reverse=True)
    a= score_list[:K]
    print("#{} {}".format(tc+1,sum(a)))