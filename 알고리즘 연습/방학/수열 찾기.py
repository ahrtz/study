import copy
T= int(input())
for tc in range(T):
    num_list = list(map(int,input().split()))

    N = int(input())
    pan=[]
    for _ in range(N):
        pan.append(list(map(int,input().split())))
    sp=[]
    for r in range(N):
        for c in range(N):
            if pan[r][c]==num_list[1]:
                sp.append((r,c))
    cnt=1
    d = ((1,0),(0,-1),(-1,0),(0,1))
    flag=0
    flag2=0
    result = 0
    for i in sp:
        startr = i[0]
        startc = i[1]
        visited=[]
        togo = [(startr,startc)]
        check_list = copy.deepcopy(num_list[1:])
        check_list.pop(0)
        while len(check_list) != 0 and cnt != num_list[0]:
            for k in range(4):
                newr = startr + d[k][0]
                newc = startc + d[k][1]
                # if len(check_list)==0:
                    
                if 0<=newr<N and 0<=newc<N and pan[newr][newc]==check_list[0] and (newr,newc) not in visited:
                    togo.append((newr,newc))
                    visited.append((newr,newc))
                    cnt += 1
                    check_list.pop(0)
                    flag = 0
                    startr = newr
                    startc = newc
                    if len(check_list)==0:
                        result = 1 
                        flag2 = 123
                elif 0<=newr<N and 0<=newc<N and pan[newr][newc]!=check_list[0]:
                    flag += 1
                if len(togo)==0:
                    flag2 = 123
                if flag == 4 :
                    cnt -= 1
                    startr,startc = togo.pop()
                    flag=0
                if flag2 ==123:
                    break 
            if flag2 == 123:
                break
    print("#{} {}".format(tc+1,result))