T=int(input())
for tc in range(T):
    N=int(input())
    pan=[list(map(int,input().split())) for _ in range(N)]
    d=[(1,0),(0,1),(-1,0),(0,-1)]
    result=[]
    maxcnt=0
    for r in range(N):
        for c in range(N):
            flag = 0
            flag1=0
            togo=[]
            visited=set([])
            cnt=1
            spr,spc = r,c
            togo.append((r,c,cnt))
            visited.add((r,c))
            while True:
                val = pan[spr][spc]
                for i in range(4):
                    newr = spr + d[i][0]
                    newc = spc + d[i][1]
                    if 0<=newr<N and 0<=newc<N and pan[newr][newc]==val+1 and (newr,newc) not in visited:
                        cnt+=1
                        visited.add((newr,newc))
                        togo.append((newr,newc,cnt))
                        flag=0
                        spr = newr
                        spc = newc
                        val+=1
                    elif flag ==4:
                        if cnt >= maxcnt:
                            finalr=r
                            finalc=c
                            maxcnt=cnt
                            result.append((pan[finalr][finalc],maxcnt))
                        if len(togo)==0:
                            flag1=156321
                            break
                        else:
                            spr,spc,cnt=togo.pop()
                        
                    else:
                        flag += 1
                if flag1==156321:
                    break
    # result=list(result)
    result.sort(key= lambda x: (x[1],-x[0]),reverse=True)
    print("#{} {}".format(tc+1," ".join(repr(k) for k in result[0])))
    # print("#{} {} {}".format(tc+1,result,maxcnt))
    # print(result)