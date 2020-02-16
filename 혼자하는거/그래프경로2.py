def find_route(a,b):
    global result
    visited[a]=1
    if a==b:
        result = 1
        return
    else:
        for v in range(1,V+1):
            if pan[a][v] == 1 and visited[v]==0:
                # print(v)
                find_route(v,b)
    return 0 



T= int(input())
for tc in range(T):
    V,E = map(int,input().split())
    pan = [[0]*(V+1) for _ in range(V+1)]
    result = 0
    visited=[0]*(V+1)
    for _ in range(E):
        st,ed = map(int,input().split())
        pan[st][ed]=1
    # print(pan)
    start , end = map(int,input().split())
    find_route(start,end)
    # print()
    
    print(f"#{tc+1} {result}")