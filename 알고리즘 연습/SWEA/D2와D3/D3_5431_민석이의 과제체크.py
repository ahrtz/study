T=int(input())
for tc in range(T):
    N,M=map(int,input().split())
    m_list=list(map(int,input().split()))
    al=list(range(1,N+1))
    res=[]
    for i in al:
        if i not in m_list:
            res.append(i)
    print("#{} {}".format(tc+1," ".join(repr(k) for k in res)))
