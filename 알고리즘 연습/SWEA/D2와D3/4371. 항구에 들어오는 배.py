T=int(input())


for tc in range(T):
    N=int(input())
    a=[1]*5000
    tmp=[]
    for _ in range(N):
        d=int(input())
        tmp.append(d)
    tmp1=[]
    for i in range(len(tmp)-1):
        tmp1.append(abs(tmp[i]-tmp[i+1]))
    print("#{} {}".format(tc+1,len(set(tmp1))))