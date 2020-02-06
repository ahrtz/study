import pprint
T=int(input())
for tc in range(T):
    N,M = map(int,input().split())
    pan=[[0]*N for _ in range(N)]
    tmp=N//2
    pan[tmp][tmp] = 2
    pan[tmp-1][tmp-1] = 2
    pan[tmp-1][tmp] = 1
    pan[tmp][tmp-1] = 1

pprint.pprint(pan)