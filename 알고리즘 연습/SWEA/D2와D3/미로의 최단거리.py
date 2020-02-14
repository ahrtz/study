def inbox(a,b): # 많이 쓰이지 않을까?
    return 0<=a<N and 0<=b<N and(miro[a][b]==0 or miro[a][b]==3)

def route(start_x,start_y):
    global cnt_list,cnt
    if miro[start_x][start_y]==3:
        cnt_list.append(cnt)
        print(visit)
        return 
    visit.append((start_x,start_y))
    for k in range(4):
        new_x = start_x+dx[k]
        new_y = start_y+dy[k]
        if visit ==[]:
            return
        if inbox(new_x,new_y) and (new_x,new_y) not in visit:
            
            cnt+=1
            route(new_x,new_y)  
            
            cnt-=1

T=int(input())
for tc in range(T):
    N=int(input())
    miro=[]
    for _ in range(N):
        miro.append(list(map(int,input())))
    sp=[]
    cnt=0
    cnt_list=[]
    visit=[]
    for r in range(N):
        for c in range(N):
            if miro[r][c]==2:
                sp.append((r,c))
    
    
    dx=[1,0,0,-1]
    dy=[0,1,-1,0]
    
    route(sp[0][0],sp[0][1])
    
    for i in range(len(cnt_list)):
        cnt_list[i] -= 1
    print(cnt_list)
    # if len(cnt_list) == 0:
    #     print("#{} {}".format(tc+1,-1))
    # else:
    #     print("#{} {}".format(tc+1,min(cnt_list)))
    
    