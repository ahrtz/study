T=int(input())
for tc in range(T):
    N,M = map(int,input().split())
    pan=[]
    for i in range(N):
        tmp = list(map(int,input().split()))
        pan.append(tmp)
    res=[]
    counted=[]
    for row in range(N):# 행 검색
        cnt=0
        for col in range(N):
            if pan[row][col]==1:
                cnt+=1
            else:
                res.append(cnt)
                cnt=0
        res.append(cnt)
    for col in range(N):#열 검색
        cnt=0
        for row in range(N):
            if pan[row][col]==1:
                cnt+=1
            else:
                res.append(cnt)
                cnt=0
        res.append(cnt)



            
    print("#{} {}".format(tc+1,res.count(M)))

        
    # ㅇㅣ제 검색
    #가로 먼저
    # delta= [(1,0),(0,1)]
    # res=[]
    # for l in range(N):
    #     for k in range(N):
            
    #         if pan[l][k]==1:
    #             if l==0 or k==0:
    #                 pass
    #             if 0<=l-1<N and 0<=k-1<N and (pan[l-1][k]!=1 or pan[l][k-1]!=1):
                               
    #                 for m in range(2): # 가로선
    #                     dx,dy = delta[m]
    #                     nx,ny = l + dx, k + dy
    #                     cnt=1
    #                     cnta=[]    
    #                     while True:

    #                         if nx>N-1 or ny>N-1:
    #                             break
                                            
    #                         if pan[nx][ny]==1:
    #                             cnt+=1
    #                         if pan[nx][ny]==0 or nx==N-1 or ny==N-1:
                                
    #                             res.append(cnt)    
    #                             break
                        
    #                         nx,ny = nx+dx,ny+dy
                    
    # print(res)