T=int(input())
for tc in range(T):
    # pan = [[0]*2001 for _ in range(2001)]
#방향 0 상 1 하 2좌 3우
# -1000 0 3 5
# 1000 0 2 3
# 0 1000 1 7
# 0 -1000 0 9
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
    while set(e) !={0}:
        for i in range(len(rc)):
            if dire[i]==0:
                # if rc[i][1]==0:
                #     pass
                rc[i][1] += 0.5
                if rc[i][1]>1000:
                    rc[i][0]=0
                    # rc.pop(i)
                    rc[i][1]=12345678
                    e[i]=0
                    # e.pop(i)
                    
            elif dire[i]==1:
                # if rc[i][0]==0:
                #     pass
                rc[i][1] -= 0.5
                if rc[i][1] < -1000:
                    rc[i][0]=0
                    rc[i][1]=-123456789
                    # rc.pop(i)
                    e[i]=0
                    # e.pop(i)
            elif dire[i]==2:
                # if rc[i][0]==0:
                #     pass
                rc[i][0] -= 0.5
                if rc[i][0] < -1000:
                    rc[i][0]=-1234567
                    rc[i][1]=0
                    # rc.pop(i)
                    e[i]=0
                    # e.pop(i)
            elif dire[i]==3:
                # if rc[i][0]==0:
                #     pass
                rc[i][0] += 0.5
                if rc[i][0] > 1000:
                    rc[i][0]=12345678
                    rc[i][1]=0
                    # rc.pop(i)
                    e[i]=0
                    # e.pop(i)
        #여기서 시작
        rc = [tuple(j) for j in rc]
        # if rc[0][0]==-1:
            # print("#")
        if len(set(rc))!=len(rc):
            used=[0]*len(rc)
            for i in range(len(rc)):
                temp = rc.pop(i)
                if temp in rc:
                    used[i] += 1
                rc.insert(i,temp)
            tmp=[]
            for k in range(len(used)):
                if used[k]>=1:
                    tmp.append(k)
            for m in range(len(tmp)):
                z=tmp.pop()
                cnt += e[z]
                e[z]=0
                rc.pop(z)
                dire.pop(z)
            if used.count(0)==1:
                break
        rc=[list(j) for j in rc]
    print("#{} {}".format(tc+1,cnt))   
            