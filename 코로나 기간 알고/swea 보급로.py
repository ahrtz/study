from collections import deque
dx=[0,1,0,-1]
dy=[1,0,-1,0]


T= int(input())
for tc in range(T):
    N=int(input())
    pan=[]
    visited=[[float('inf')]*N for _ in range(N)]
    for _ in range(N):
        tmp =list(map(int,input()))
        pan.append(tmp)
    visited[0][0]=0
    sp=deque()
    sp.append([0,0]) # r,c,cnt
    while sp: # 그냥 인접한 것중에 왓던곳 제끼고 가야 할 곳중 
        r,c = sp.popleft()
        tmp=[]
        for i in range(4):
            newr=r+dx[i]
            newc=c+dy[i]
            if 0<=newr<N and 0<=newc<N and pan[newr][newc]+visited[r][c]<visited[newr][newc]:
                visited[newr][newc]=pan[newr][newc]+visited[r][c]
                sp.append([newr,newc])
    print(f"#{tc+1} {visited[N-1][N-1]}")      
