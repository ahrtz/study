def find_route(st_r,st_c,pan):
    global result


    if pan[st_r][st_c]==3:
        result = 1 
        return

    visit.append((st_r,st_c))
    
    for i in range(4):
        newr = st_r + d[i][0]
        newc = st_c + d[i][1]
        if (newr,newc) not in visit and pan[newr][newc]!=1:
            
            find_route(newr,newc,pan)
            
        



for _ in range(10):
    T = int(input())
    pan=[]
    for _ in range(16):
        tmp = list(map(int,input()))
        pan.append(tmp)
    
    for r in range(16):
        for c in range(16):
            if pan[r][c]==2:
                sp = (r,c)
    d=((1,0),(0,1),(-1,0),(0,-1))
    result = 0
    visit=[]
    find_route(sp[0],sp[1],pan)
    print("#{} {}".format(T,result))