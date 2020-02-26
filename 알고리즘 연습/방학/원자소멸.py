T=int(input())
for tc in range(T):
    # pan = [[0]*2001 for _ in range(2001)]
#방향 0 상 1 하 2좌 3우

    N = int(input())
    rc=[]
    dire=[]
    e=[]
    for _ in range(N):# x좌표 y좌표 이동방향 보유에너지
        r_tmp,c_tmp,dire_tmp,E_tmp = map(int,input().split())
        rc.append([r_tmp,c_tmp])
        dire.append(dire_tmp)
        e.append(E_tmp)
    
    
    
    cnt = 0
    while set(e) !={0}: # 시간초과 나니까 위에서 걸러보자 어떠ㅗㅎ게..?
        check=[0]*len(rc)
        for i in range(len(rc)):
            if dire[i]==0:
                
                rc[i][1] += 0.5
                if rc[i][1]>1000:
                    check[i]=1
                    
            elif dire[i]==1:
                # if rc[i][0]==0:
                #     pass
                rc[i][1] -= 0.5
                if rc[i][1] < -1000:
                    check[i]=1
            elif dire[i]==2:
                # if rc[i][0]==0:
                #     pass
                rc[i][0] -= 0.5
                if rc[i][0] < -1000:
                    check[i]=1
            elif dire[i]==3:
                # if rc[i][0]==0:
                #     pass
                rc[i][0] += 0.5
                if rc[i][0] > 1000:
                    check[i]=1
        #여기서 시작
        for mm in range(len(check)-1,-1,-1): # 넘는거 제거하기
            if check[mm]==1:
                rc.pop(mm)
                e.pop(mm)
                dire.pop(mm)
        
        used=[0]*len(rc)
        for i in range(len(rc)):
            temp = rc.pop(i)
            if temp in rc:
                used[i] += 1
            rc.insert(i,temp)
        tmp=[]
        if 1 in used:
            for k in range(len(used)):
                if used[k]>=1:
                    tmp.append(k)
            for m in range(len(tmp)):
                z=tmp.pop()
                cnt += e[z]
                # e[z]=0
                e.pop(z)
                rc.pop(z)
                dire.pop(z)
        if len(rc)<=1:
            break
    
    print("#{} {}".format(tc+1,cnt))   
            