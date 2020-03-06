T= int(input())
for tc in range(T):
    N= int(input())
    pan = [list(map(int,input().split())) for _ in range(N)]
    d=[(1,1),(1,-1),(-1,-1),(-1,1)]
    # cnt=0
    result=[]
    tmp=[]
    for r in range(N):
        for c in range(1,N-1):
            set_list=[]
            visited=[]
            set_list.append(pan[r][c])
            visited.append((r,c))
            flag=0
            i=0
            togo=[(r,c,set_list)]
            spr,spc=r,c
            while togo: # 백트래킹해야댐
                newr = spr+d[i][0]
                newc = spc+d[i][1]
                if 0<=newr<N and 0<=newc<N :
                    if i==3 and newr==r and newc==c:
                        break
                    
                    elif pan[newr][newc] not in set_list and ((newr,newc))not in visited:
                        set_list.append(pan[newr][newc])
                        visited.append((newr,newc))
                        togo.append((newr,newc,set_list))
                        spr=newr
                        spc=newc
                        flag=0
                    else:
                        i+=1
                        flag+=1
                if flag==3:
                    i-=1
                    flag=0
                    spr,spc,set_list=togo.pop()
                elif newr<0 or newr>=N or newc<0 or newc>=N:
                    i+=1
                    flag+=1
            print(set_list)
            print(visited)
    # if len(result)==0:
    #     print("#{} {}".format(tc+1,-1))
    # else:
    #     print("#{} {}".format(tc+1,max(result)))

