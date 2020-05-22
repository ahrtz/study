from collections import deque
T=int(input())
for tc in range(T):
    r=int(input())
    pan=[]
    for _ in range(r):
        pan.append(list(map(int,input().split())))
    sp=[0,0]
    ed=[r-1,r-1]
    