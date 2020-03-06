import pprint
def bfs(a,b):
    global cnt,visited
    if a == b:
        print("#{} {}".format(tc+1,cnt))
    else:
        for i in range(V+1):
            if pan[a][i]==1 and not visited[i]:
                visited[i]=1
                cnt+=1
                bfs(i,b)
                cnt-=1
                visited[i]=0


T=int(input())
for tc in range(T):
    V,E = map(int,input().split())
    visited = [0]*(V+1)
    pan= [[0]*(V+1) for _ in range(V+1)]
    cnt = 0 
    for _ in range(E):
        i,j = map(int,input().split())
        pan[i][j]=1
        pan[j][i]
    sp,ep = map(int,input().split())
    bfs(sp,ep)