T=int(input())
for tc in range(T):
    W,H,N = map(int,input().split())
    mv_list=[]
    for _ in range(N):
        sp,ep = map(int,input().split())
        mv_list.append((sp,ep))
    cnt=0
    for i in range(N-1):# 시작 도착 계속 뽑기 
        diff_x = mv_list[i][0]-mv_list[i+1][0]
        diff_y = mv_list[i][1]-mv_list[i+1][1]
        # while diff_x!=0 or diff_y!=0:
        if diff_x * diff_y <=0: # 두개의 곱이 0이거나 음수면 그냥 직선이동
            cnt += (abs(diff_x)+abs(diff_y))
            diff_x = 0
            diff_y = 0
        else: # 아니면 대각이 존재
            cnt += max(abs(diff_x),abs(diff_y))
                # if diff_x>0 and diff_y>0:
                #     diff_x-=1
                #     diff_y-=1
                #     cnt += 1
                # elif diff_x<0 and diff_y<0:
                #     diff_x+=1
                #     diff_y+=1
                #     cnt += 1
    print("#{} {}".format(tc+1,cnt))
