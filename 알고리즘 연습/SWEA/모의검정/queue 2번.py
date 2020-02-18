T=int(input())
for tc in range(T):
    N=int(input())
    miro=[]
    for _ in range(N):
        tmp = list(map(int,input()))
        miro.append(tmp)
    for r in range(N):
        for c in range(N):
            if miro[r][c]==2:
                sp=(r,c)
            if miro[r][c]==3:
                ed=(r,c)

    togo=[]
    visited=[]
    startx = sp[0]
    starty = sp[1]
    d=((0,1),(1,0),(0,-1),(-1,0))
    cnt=10
    for i in range(4):
        newx=startx + d[i][0]
        newy = starty + d[i][1]

        if 0<=newx<N and 0<=newy<N and miro[newx][newy]==0:
            miro[newx][newy]=cnt   
            togo.append((newx,newy))
            visited.append((newx,newy))

    while togo!=[]:
        startx1,starty1=togo.pop(0)
        
        for i in range(4):
            newx=startx1 + d[i][0]
            newy=starty1 + d[i][1]
            if 0<=newx<N and 0<=newy<N and (miro[newx][newy]==0 or miro[newx][newy]==3):
                miro[newx][newy]=miro[startx1][starty1]+1
                togo.append((newx,newy))
                visited.append((newx,newy))

    if miro[ed[0]][ed[1]] ==3:
        print("#{} {}".format(tc+1,0))
    else:
        print("#{} {}".format(tc+1,miro[ed[0]][ed[1]]-10))