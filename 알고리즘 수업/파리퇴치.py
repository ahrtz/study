a=int(input())
for i in range(a):
    N, M= map(int,input().split())
    pan=[]
    for k in range(N):
        pan.append(list(map(int,input().split())))
    #파리채 공간
    final=[]
    for l in range(N-(M-1)):
        
        for k in range(N-(M-1)):
            tmp=[]
            for garo in range(M):
                for sero in range(M):
                    tmp.append(pan[l+garo][k+sero])
            final.append(sum(tmp))
    
    print("#{} {}".format(i+1,max(final)))
