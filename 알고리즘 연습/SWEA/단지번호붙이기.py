def check(x,y):
    global cnt
    apart[x][y] = 0
    cnt += 1 
    for i in range(4):
        dr,dc = d[i][0],d[i][1]
        newr = x + dr
        newc = y + dc 
        if newr < 0 or newr>=N or newc<0 or newc>=N:
            continue
        if apart[newr][newc]==1:
            # print(newr,newc)
            check(newr,newc)

N=int(input())
apart=[]
for _ in range(N):
    tmp = list(map(int,input()))
    apart.append(tmp)

d=((-1,0),(0,1),(1,0),(0,-1))
tmp=[]
for row in range(N):
    for col in range(N):
        if apart[row][col]==1:
            cnt = 0
            check(row,col)
            tmp.append(cnt)
tmp =sorted(tmp)
print(len(tmp))
for i in tmp:
    print(i)
