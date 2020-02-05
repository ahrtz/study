import pprint
T=int(input())
for tc in range(T):
    width = int(input())
    pan = [[0]*width for _ in range(width)]
    for i in range(width):
        tmp = list(map(int,input().split()))
        for j in range(len(tmp)):
            pan[i][j]=tmp[j]
    started=[]
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    
        