# 5 6
# 1 2 
# 1 3
# 3 2
# 2 5
# 3 4
# 5 4
def dfs(n,V):
    visited[n]=1 # n번 노드에 방문 표시
    print(n,end=" ") # n번 노드에서 할 일
    for i in range(1,V+1): # 모든 노드 i에 대해
        if pan[n][i]==1 and visited[i]==0:# n에 인접하고 방문하지 않았으면
            dfs(i,V) # i노드로 이동

def dfs2(n,V):
    s=[]
    used = [0]*(V+1)
    s.append(n)
    used[n]=1
    while len(s)!= 0 : # 스택이 비어 있지 않으면
        n=s.pop() # pop(), 갈 수 있는 노드중 하나를 꺼내 그곳으로 이동
        print(n, end=" ")
        for i in range(1,V+1):
            if pan[n][i] == 1 and used[i] == 0 : # i 가 인접이고 스택에 들어있지 않으면
                s.append(i)
                used[i] = 1



n , m = map(int,input().split())
pan=[[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    pan[a][b]=1
    # pan[b][a]=1 # 방향성이 없으면 
dfs(1,n)