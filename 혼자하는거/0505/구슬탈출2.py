a,b = map(int,input().split())

pan=[]

# 왼 아래 오 위
d=[(0,-1),(1,0),(0,1),(-1,0)]


for i in range(a):
    pan.append(list(input().strip()))

for x in range(a):
    for y in range(b):
        if pan[x][y]=='R':
            pan[x][y]='.'
            Rx,Ry=x,y
        if pan[x][y]=='B':
            pan[x][y]='.'
            Bx,By=x,y
        if pan[x][y]=='O':
            goal = (x,y)
# 여기서 부터 돌릴거
starts=[((Rx,Ry,0,0),(Bx,By,0))]
while starts:
    red,blue =starts.pop(0)
    for i in range(4):
        tmprx,tmpry ,tmprcnt,totalrcount= red
        tmpbx,tmpby,tmpbcnt = blue
        while pan[tmprx][tmpry]!="#" and pan[tmprx][tmpry]!='O':
            tmprx = tmprx + d[i][0]
            tmpry = tmpry+d[i][1]
            tmprcnt += 1 
        while pan[tmpbx][tmpby]!="#" and pan[tmpbx][tmpby]!='O':
            tmpbx = tmpbx + d[i][0]
            tmpby = tmpby+d[i][1]
            tmpbcnt += 1 
        if tmpbx==tmprx & tmpby==tmpry:
            if tmpbcnt>tmprcnt:
                tmpbx = tmpbx-d[i][0]
                tmpby = tmpby - d[i][1]
            else:
                tmprx = tmprx-d[i][0]
                tmpry= tmpry-d[i][1]
        
