import heapq
T=int(input())
for tc in range(T):
    V,E = map(int,input().split())
    pan={i:[] for i in range(V+1)}
    for i in range(E):
        s,e,w = map(int,input().split())
        pan[s].append([e,w])
        pan[e].append([s,w])
    # print(pan)
    INF=float('inf')
    key=  [INF]*(V+1)
    visited=[0]*(V+1)
    pq=[]
    key[0]=0

    heapq.heappush(pq,(0,0)) # 첫번째 요소가 key 두번째가 노드번호
    result=0
    while pq:
        k,node = heapq.heappop(pq)
        if visited[node]==1:
            continue
        visited[node]=1
        result+=k
        for arrive,wt in pan[node]:
            # print(arrive,visited[arrive],key[arrive])
            if visited[arrive]==0 and key[arrive]>wt:
                # print(arrive,'$')
                key[arrive]=wt
                heapq.heappush(pq,(key[arrive],arrive))
    print(f'#{tc+1} {result}')