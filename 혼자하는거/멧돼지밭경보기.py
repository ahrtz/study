T=int(input())
for tc in range(T):
    N=int(input())
    tmp=[]
    for _ in range(N):
        tmp.append(list(map(int,input().split())))
    alert=[] # 경보기 위치 뽑기
    for row in range(N):
        temp=[]
        for col in range(N):
            if tmp[row][col]==1:
                temp.append((row,col))

        if len(temp)!=0:    
            alert.append(temp)
    # 첫 경보기의 0번 -1 번 마지막 경보기의 0번 -1 번 사용
    cnt=0
    #왼위
    
    for row in range(0,alert[0][0][0]+1):
        for col in range(0,alert[0][0][1]+1):
            if tmp[row][col]==2:
                cnt+=1
    #오위
    for row in range(0,alert[0][-1][0]+1):
        for col in range(alert[0][-1][1],N):
            if tmp[row][col]==2:
                cnt+=1
    #왼 아래
    for row in range(alert[-1][0][0],N):
        for col in range(alert[-1][0][1]+1):
            if tmp[row][col]==2:
                cnt+=1
    #오 아래
    for row in range(alert[-1][-1][0],N):
        for col in range(alert[-1][-1][1],N):
            if tmp[row][col]==2:
                cnt+=1
    print("#{} {}".format(tc+1,cnt))