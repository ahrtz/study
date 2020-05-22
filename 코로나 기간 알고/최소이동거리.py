T=int(input())
for tc in range(T):
    V,E = map(int,input().split())
    adj = {i:[] for i in range(V+1)}
    for i in range(E):
        s,e,c = map(int,input().split())
        adj[s].append([e,c])

    INF = float('inf')
    dist=[INF]*(V+1)
    selected = [False]*(V+1)
    dist[0]=0
    cnt=0
    while cnt<V+1:
        min = INF
        u=-1
        for i in range(V+1):
            if not selected[i] and dist[i]<min:
                min = dist[i]
                # print(dist,dist[i],i,156)
                u=i
        selected[u]=True
        # print(min)
        cnt+=1

        for w ,cost in adj[u]:
            if dist[w]>dist[u]+cost:
                dist[w] = dist[u]+cost
    print(f"#{tc+1} {dist[-1]}")