T=int(input())
for tc in range(T):
    V,E = map(int,input().split())
    pan = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        n1,n2,w = map(int,input().split())
        pan[n1][n2] = w
        pan[n2][n1] = w
    # print(pan)
    INF = float('inf')
    key=[INF]*(V+1)
    p=[-1]*(V+1)# 부모를 알려주는 배열 
    visited=[0]*(V+1)
    key[0]=0
    cnt=0
    result=0
    while cnt<(V+1):# 즉 이건 순차탐색 해나가는거네 다 돌면서 
        min =INF
        u=-1
        for i in range(V+1):
            if visited[i]==0 and key[i]<min: # 최소값 찾기 
                min=key[i]
                u=i
        visited[u]=1
        result+=min
        cnt+=1

        for w in range(V+1):
            if pan[u][w]>0 and not visited[w] and key[w]>pan[u][w]:
                key[w] = pan[u][w]
                p[w] = u
    print(f"#{tc+1} {result}")
