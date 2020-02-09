import itertools
T=int(input())
for tc in range(T):
    N = list(map(int,input().split()))
    
    alpha = list(itertools.combinations(N,3))
    res=[]
    for i in range(len(alpha)):
        res.append(sum(alpha[i]))
    res=sorted(set(res))
    
    print("#{} {}".format(tc+1,res[-5]))