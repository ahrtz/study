def DFS_visit(adj, u, visited):
    visited.append(u)
    # print("#")
    for v in range(N+1):
        if adj[u][v]==1 and v not in visited:
            print(v)
            DFS_visit(adj, v, visited)
 
 
def DFS(adj, s):
    visited =[]
    DFS_visit(adj, s, visited)
    return visited


T=int(input())
for tc in range(T):
    N,E = map(int,input().split())
    pan=[[0]*(N+1) for _ in range(N+1)]
    
    for _ in range(E):
        start, end = map(int,input().split())
        pan[start][end]=1
    # print(pan)
    print("#{} {}".format(tc+1," ".join(str(k) for k in DFS(pan,0))))