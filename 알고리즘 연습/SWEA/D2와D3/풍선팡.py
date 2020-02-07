T=int(input())
for tc in range(T):
    N,M = map(int,input().split())
    pan=[]
    for i in range(N):
        pan.append(list(map(int,input().split())))
    
    cnt_list=[]
    delta=((1,0),(2,0),(-1,0),(-2,0),(0,0),(0,1),(0,2),(0,-1),(0,-2))
    while True:
        cnt=0
        for row in range(N):
            for col in range(M):
                for d in range(len(delta)):
                    dx,dy =delta[d]
                    newrow=row+dx
                    newcol=col+dy
                    try 
                