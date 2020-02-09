T=int(input())
for tc in range(T):
    N,M = map(int,input().split())
    pan=[]
    for i in range(N):
        pan.append(list(map(int,input().split())))
    
    cnt=0
    cnt_list=[]
    delta=((1,0),(-1,0),(0,1),(0,-1))
    while len(cnt_list)<(N*M):
        
        for row in range(N):
            for col in range(M):
            
                for d in range(len(delta)):
                    for ti in range(1,pan[row][col]+1):
                        dx,dy =delta[d]
                        newrow=row+dx*ti
                        newcol=col+dy*ti
                        if 0<=newcol<M and 0<=newrow<N:
                            cnt+= pan[newrow][newcol]
                cnt+=pan[row][col]            
                cnt_list.append(cnt)
                cnt=0
    print("#{} {}".format(tc+1,max(cnt_list)))