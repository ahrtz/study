T= int(input())
for tc in range(T):
    N=int(input())
    busstop=[0]*5001
    for i in range(N):
        a,b=map(int,input().split())
        for k in range(a,b+1):
            busstop[k]+=1
    
    P = int(input())
    res=[]
    for pp in range(P):
        aa = int(input())
        res.append(busstop[aa])
    print("#{} {}".format(tc+1," ".join(repr(m) for m in res)))
