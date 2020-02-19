T=int(input())
for tc in range(T):
    N=int(input())
    pan=[]
    for _ in range(N):
        tmp = list(map(int,input()))
        pan.append(tmp)
    for r in range(N):
        for c in range(N):
            if pan[r][c]==2: # 시작점 좌표 받고 변경해놓기
                spr,spc = r,c
    d=((0,1),(1,0),(0,-1),(-1,0))
    cnt=0
    visited=[] # 기록 비교용
    #뽑기용
    togo=[(spr,spc,cnt)]
    cnt=0
    
    cnt_save=[]
    flag=0
    while togo!=[]:
        for i in range(4):
            start_r = spr + d[i][0]
            start_c = spc + d[i][1]
            if start_r<0 or start_c <0 or start_r>=N or start_c>= N:
                continue
            if pan[start_r][start_c]==3:
                cnt_save.append(cnt)
                cnt=0 # 저장후 초기화
                spr,spc,cnt=togo.pop(0)# 시작점 안간곳 있나 체크 
                
                flag = 0 # 초기화
            if pan[start_r][start_c]==0 and (start_r,start_c) not in visited:
                visited.append((start_r,start_c))
                
                cnt+=1
                togo.append((start_r,start_c,cnt))
                spr = start_r
                spc = start_c
                flag = 0
            if flag ==4:
                spr,spc,cnt=togo.pop(0)
                flag = 0 # 
            if (start_r,start_c) in visited:
                flag +=1
        
    if len(cnt_save)==0:
        print("#{} {}".format(tc+1,-1))    
    else:
        print("#{} {}".format(tc+1,min(cnt_save)))