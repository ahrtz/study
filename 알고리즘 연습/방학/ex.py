T=int(input())
for tc in range(T):
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
    while True: # 시간초과 나니까 위에서 걸러보자 어떠ㅗㅎ게..?
        check=[0]*len(rc)
        for i in range(len(rc)):
            if dire[i]==0:
                rc[i][1] += 0.5
                if rc[i][1]>1000:
                    check[i]=1
            elif dire[i]==1:
                rc[i][1] -= 0.5
                if rc[i][1] < -1000:
                    check[i]=1
            elif dire[i]==2:
                rc[i][0] -= 0.5
                if rc[i][0] < -1000:
                    check[i]=1
            elif dire[i]==3:
                rc[i][0] += 0.5
                if rc[i][0] > 1000:
                    check[i]=1
        #여기서 시작
        if 1 in check:
            for mm in range(len(check)-1,-1,-1): # 넘는거 제거하기
                if check[mm]==1:
                    rc.pop(mm)
                    e.pop(mm)
                    dire.pop(mm)
        rc = list((map(tuple, rc)))
        if len(rc)!=len(set(rc)):
            used=[0]*len(rc)
            for i in range(len(rc)): # 같은거 체크하기 
                temp = rc.pop(i)
                if temp in rc:
                    used[i] += 1
                rc.insert(i,temp)
            
            if 1 in used:
                for k in range(len(used)-1,-1,-1):
                    if used[k]>=1:
                        cnt += e[k]
                        # e[z]=0
                        e.pop(k)
                        rc.pop(k)
                        dire.pop(k)
        if len(rc)<=1:
            break
        rc = list((map(list, rc)))
    print("#{} {}".format(tc+1,cnt))   
            