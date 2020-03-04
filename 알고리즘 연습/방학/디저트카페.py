T= int(input())
for tc in range(T):
    N= int(input())
    pan = [list(map(int,input().split())) for _ in range(N)]
    d=[(1,1),(1,-1),(-1,-1),(-1,1)]
    # cnt=0
    result=[]
    for r in range(N):
        for c in range(1,N-1):
            set_list=set([])
            visited=[]
            set_list.add(pan[r][c])
            visited.append((r,c))
            togo=[(r,c)]
            flag=0
            i=0
            spr,spc=r,c
            while i<4:
                
                newr=spr+d[i][0]
                newc=spc+d[i][1]
                if 0<=newr<N and 0<=newc<N:
                    if i==3 and newr==r and newc ==c:
                        # set_list.add(pan[r][c])
                        break
                    
                    elif flag ==4:
                        if not togo:
                            break
                        i += 1
                        # set_list.remove(pan[newr][newc])
                        flag = 0
                        spr,spc = togo.pop()
                        
                    elif pan[newr][newc] not in set_list :
                        if (newr,newc) not in visited:
                            set_list.add(pan[newr][newc])
                            visited.append((newr,newc))
                            togo.append((newr,newc))
                            spr = newr
                            spc = newc
                            flag = 0
                    elif pan[newr][newc] in set_list:
                        flag+=1
                    else:
                        continue
                elif newr<0 or newr>=N or newc<0 or newc>=N:
                    i+=1
            # set_list.add(pan[r][c]) //
            print(visited)
            print(set_list)
            if len(set_list)%2==0 and len(set_list)>=4 and len(set_list)==len(visited) :
                if abs(visited[-1][0]-r)==1 and abs(visited[-1][1]-c)==1:
                    result.append(len(set_list))
    if len(result)==0:
        print("#{} {}".format(tc+1,-1))
    else:
        print("#{} {}".format(tc+1,max(result)))

#try except 쓰면 될것같은데 술먹엇으니 내일 
# 방향을 픽스하고 돌리기 try except 로 조건 충족하면 돌리기 
#visited 를 set 으로 만들거나 cnt 에 +1 하기 