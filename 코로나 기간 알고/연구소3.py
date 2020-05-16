from collections import deque
from itertools import combinations 
import pprint

def bfs(virus_list):
    dist = [[-1] * N for _ in range(N)]
    dq=deque()
    for pos in virus_list:
        dq.append(pos)
        dist[pos[0]][pos[1]] = 0
    max_dist=0
    while dq:
        x,y=dq.popleft()
        for k in range(4):
            nx=x+dir[k][0]
            ny=y+dir[k][1]

            if 0<=nx<N and 0<=ny<N and pan[nx][ny]!=1 and dist[nx][ny]==-1:
                dist[nx][ny]=dist[x][y]+1
                if pan[nx][ny]==0:
                    max_dist=max(max_dist,dist[nx][ny])
                dq.append([nx,ny])

    tmp=[]
    for i in dist:
        tmp+=i
    # print(a)
    # pprint.pprint(dist)
    # print(max_dist)
    tmp_pan =[]
    for k in pan:
        tmp_pan+=k

    if tmp.count(-1)==tmp_pan.count(1):	# 벽의 개수랑 안간 곳 갯수 
        ans.append(max_dist)	

N,M = map(int,input().split())
pan = [list(map(int,input().split())) for _ in range(N)]
dir = [[1,0],[0,1],[-1,0],[0,-1]]

virus_pos=deque()
ans=[]
for i in range(N):
    for j in range(N):
        if pan[i][j]==2:
            virus_pos.append([i,j])

for now_virus_list in combinations(virus_pos,M):
    bfs(now_virus_list)

print(min(ans) if ans else -1)