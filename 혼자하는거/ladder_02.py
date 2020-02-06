for i in range(10):
    Tc=int(input())
    ladder=[]
    for _ in range(100):
        tmp = list(map(int,input().split()))
        ladder.append(tmp)
    #시작점의 좌표 빼서 저장
    start_point=[]
    for j in range(100):
        if ladder[0][j]==1:
            start_point.append(j)
    res=[]
    for start in range(len(start_point)):
        start_y=0
        start_x=start_point[start]
        cnt=0
        visit=[]
        #왼 검사 오른검사 아래검사순서
        while start_y<99:
            if 0<=start_x - 1<100 and 0<=start_y<100 and ladder[start_y][start_x-1]==1 and (start_y,start_x-1) not in visit:
                visit.append((start_y,start_x))
                start_x -=1
                cnt+=1
                
            elif 0<=start_x + 1<100 and 0<=start_y<100 and ladder[start_y][start_x+1]==1 and (start_y,start_x+1) not in visit:
                visit.append((start_y,start_x))
                start_x +=1
                cnt+=1
                
            else:
                start_y+=1
                cnt+=1
        res.append((start_point[start],cnt))
    final =sorted(res,key=lambda x: x[1]) 
    # 정렬후 결과가 똑같은것이 있는 경우 
    print(final)
    li=[]
    for fi in range(len(final)):
        if final[fi][1]==final[0][1]:
            li.append(final[fi])
    li = sorted(li,key= lambda x:x[0])
    if len(li)==1:
        print("#{} {}".format(Tc,li[0][0]))
    else:
        print("#{} {}".format(Tc,li[-1][0]))
    




