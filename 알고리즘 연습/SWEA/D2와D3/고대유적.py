T=int(input())
for tc in range(T):
    N,M = map(int,input().split())
    pan=[]
    for n in range(N):
        tmp = list(map(int,input().split()))
        pan.append(tmp)
    # 가로 탐색
    cnt_list=[]
    garo_visit=[]
    sero_visit=[]
    for row in range(N):
        for col in range(M):
            if pan[row][col]==1:
                cnt=1
                garo_visit.append((row,col))
                while True:
                    new_col = col+1
                    if new_col<M and pan[row][new_col]==1 and (row,new_col) not in garo_visit:
                        cnt+=1
                        garo_visit.append((row,new_col))
                        col=new_col
                    else:
                        if cnt > 1 :
                            cnt_list.append(cnt)
                            break
                        break
    for col in range(M):#세로탐색
        for row in range(N):
            if pan[row][col]==1:
                cnt=1
                sero_visit.append((row,col))
                while True:
                    new_row = row+1
                    if new_row<N and pan[new_row][col]==1 and (new_row,col) not in sero_visit:
                        cnt+=1
                        sero_visit.append((new_row,col)) 
                        row=new_row
                    else:
                        if cnt>1:
                            cnt_list.append(cnt)
                            break
                        break
    if len(cnt_list)<1:
        print("#{} {}".format(tc+1,0))    
    else:
        print("#{} {}".format(tc+1,max(cnt_list)))