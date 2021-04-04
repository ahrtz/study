g,s  = map(int,input().split())

pan=[]
for i in range(g):
    pan.append(list(input().strip()))
for i in range(g):
    for j in range(s):
        if pan[i][j]=="R":
            rx,ry=i,j
        if pan[i][j]=="B":
            bx,by=i,j
print(rx,ry,bx,by)