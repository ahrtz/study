T= int(input())
for tc in range(T):
    N= int(input())
    pan = [list(map(int,input().split())) for _ in range(N)]
    d=[(1,1),(-1,1),(1,-1),(-1,-1)]
    # cnt=0
    for r in range(1,N-1):
        for c in range(N-1):
            set_list=set([])
            visited=[]
            dessert = []
            spr,spc =r,c
            i=0
            set_list.add(pan[r][c])
            # visited.append((r,c))
            while i!=4:
                newr=spr+d[i][0]
                newc=spc+d[i][1]
                if 0<=newr<N and 0<=newc<N:
                    if pan[newr][newc] not in set_list and (newr,newc) not in visited:
                        set_list.add(pan[newr][newc])
                        visited.append((newr,newc))
                        spr=newr
                        spc=newc
                    elif pan[newr][newc] in set_list:
                        i += 1
                else:
                    i += 1
            print(visited,(r,c))
#try except 쓰면 될것같은데 술먹엇으니 내일 
# 방향을 픽스하고 돌리기 try except 로 조건 충족하면 돌리기 
#visited 를 set 으로 만들거나 cnt 에 +1 하기 