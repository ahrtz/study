def turn(a):
    res=[]
    for col in range(len(a)):
        tmp=[]
        for row in range(len(a)-1,-1,-1):
            tmp.append(a[row][col])
        res.append(tmp)
    return res

T=int(input())
for tc in range(T):
    n=int(input())
    pan=[]
    for _ in range(n):
        tmp = list(map(int,input().split()))
        pan.append(tmp)
    
    res=turn(pan)
    res1=turn(res)
    res2=turn(res1)
    for i in range(len(res)):
        print("".join(repr(K) for K in res[i]),"".join(repr(K) for K in res1[i]),"".join(repr(K) for K in res2[i]))