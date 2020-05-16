def track(idx,remain,cnt):
    global N, min_cnt,tmp
    remain-=1
    if cnt>min_cnt:
        return
    elif idx==N:
        if cnt<min_cnt:
            min_cnt=cnt
            return
    else:
        track(idx+1,tmp[idx],cnt+1)# 배터리를 교체하는 경우
        if remain>0:
            track(idx+1,remain,cnt)        # 배터리를 교체하지 않고 진행하는 경우



T=int(input())
for tc in range(T):
    tmp=list(map(int,input().split()))
    N=len(tmp)-1
    cnt=0
    min_cnt=10**3
    track(2,tmp[1],0)
    print(min_cnt)