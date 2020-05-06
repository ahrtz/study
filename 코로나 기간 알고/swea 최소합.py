T= int(input())
for tc in range(T):
    length = int(input())
    pan=[]
    for _ in range(length):
        pan.append(list(map(int,input().split())))
    dx=(0,1)
    dy=(1,0)
    sp =[[0,0,pan[0][0]]]
    
    tmp_ans=[]
    while sp:
        x,y,val = sp.pop()
        for i in range(len(dx)):
            newx=x+dx[i]
            newy=y+dy[i]
            newval=val
            if 0<=newx<length and 0<=newy<length:
                newval+=pan[newx][newy]
                if newx==(length-1) and newy==(length-1):
                    tmp_ans.append(newval)
                else:
                    sp.append([newx,newy,newval])
                    
                # print(newx,newy,newval)
        
        
    print(f"#{tc+1} {min(tmp_ans)}")