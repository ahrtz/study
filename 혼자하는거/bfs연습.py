
def DFS_visit(adj, u, visited):
    visited.append(u)
    for v in adj[u]:
        if v not in visited:
            DFS_visit(adj, v, visited)
 
 
def DFS(adj, s):
    visited =[]
    DFS_visit(adj, s, visited)
    return visited
 
 
G1 = {1: [2, 3], 2: [3, 4, 5], 3: [5, 7, 8], 4: [5], 5: [6], 6: [], 7: [8], 8: []}



print(G1)
print(DFS(G1, 1))