def bfs(a,b,visited):
    global cnt,Q,result
    Q.append(a)
    visited[a]=1
    while Q:
        spn=Q.pop(0)
        for i in range(V+1):
            if pan[spn][i]==1 and not visited[i]:
                Q.append(i)
                visited[i]=1
                cnt[i]=cnt[spn]+1
                if i==ep:
                    result=cnt[i]
                    return
                
    return


T=int(input())
for tc in range(T):
    V,E = map(int,input().split())
    visited = [0]*(V+1)
    pan= [[0]*(V+1) for _ in range(V+1)]
    cnt = [0]*(V+1) 
    for _ in range(E):
        i,j = map(int,input().split())
        pan[i][j]=1
        pan[j][i]=1
    sp,ep = map(int,input().split())
    Q=[]
    result=0
    bfs(sp,ep,visited)
    print("#{} {}".format(tc+1,result))