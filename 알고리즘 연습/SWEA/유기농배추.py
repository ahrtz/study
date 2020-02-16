import sys
sys.setrecursionlimit(1500)
def check(x,y):
    
    farm[x][y] = 0
    
    for i in range(4):
        dr,dc = d[i][0],d[i][1]
        newr = x + dr
        newc = y + dc 
        if newr < 0 or newr>=N or newc<0 or newc>=M:
            continue
        if farm[newr][newc]==1:
            # print(newr,newc)
            check(newr,newc)

T=int(input())
for i in range(T):
    M,N,K = map(int,input().split())
    
    farm = [[0]*M for _ in range(N)]
    # print(farm)
    for  _ in range(K):
        a,b = map(int,input().split())
        farm[b][a]=1
    

    d=((-1,0),(0,1),(1,0),(0,-1))
    tmp=[]
    # pprint.pprint(farm)
    cnt=0
    for row in range(N):
        for col in range(M):
            if farm[row][col]==1:
                cnt += 1
                
                check(row,col)
    
    print(cnt)

