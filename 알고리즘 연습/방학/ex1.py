T= int(input())
for tc in range(T):
    N= int(input())
    pan = [list(map(int,input().split())) for _ in range(N)]
    d=[(1,1),(1,-1),(-1,-1),(-1,1)]
    # cnt=0
    result=[]
    for r in range(N):
        for c in range(1,N-1):
            visited=[]
            set_list=set()
            visited.append((r,c))
            set_list.add(pan[r][c])
            togo=[]
            togo.append((r,c,set_list))
            i=0
            spr,spc=r,c
            flag=0
            while togo and i<4 :
                newr=spr + d[i][0]
                newc=spc + d[i][1]
                if 0<=newr<N and 0<=newc<N:
                    if i==3 and newr==r and newc==c:
                        break
                    
                    
                    elif pan[newr][newc] not in visited:
                        if pan[newr][newc] not in set_list:
                            togo.append((newr,newc,set_list))
                            set_list.add(pan[newr][newc])
                            visited.append((newr,newc))
                            flag=0
                            spr=newr
                            spc = newc
                        elif flag==1:
                            spr,spc,set_list=togo.pop()

                        else:
                            i+=1
                            flag+=1
                else:
                    i+=1
            print(visited)
            print(set_list)
            if len(set_list)%2==0 and len(set_list)>=4 and len(set_list)==len(visited) :
                if abs(visited[-1][0]-r)==1 and abs(visited[-1][1]-c)==1:
                    result.append(len(set_list))
            print(result)
    if len(result)==0:
        print("#{} {}".format(tc+1,-1))
    else:
        print("#{} {}".format(tc+1,max(result)))