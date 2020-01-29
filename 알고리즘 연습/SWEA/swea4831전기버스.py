T= int(input())
for i in range(T):
    K,N,M = map(int,input().split())
    bus_stop = list(map(int,input().split()))
    
    dis= [0,*bus_stop,N]
    interval=[]
    for k in range(len(dis)-1):
        interval.append(dis[k+1]-dis[k])
    
    if max(interval)>K:
        cnt = 0
    else:
        cnt = 0
        mv = 0
        tmp_mv = 0
        for l in range(1,len(interval)):
           interval[l] += interval[l-1]
        
        for m in range(len(interval)-1):
            tmp_mv=tmp_mv+3
            if tmp_mv>=interval[m] and tmp_mv<interval[m+1]:
                cnt+=1
                tmp_mv=interval[m]
                
            elif tmp_mv>=interval[m+1] and tmp_mv<interval[m+2]:
                cnt+=1
                tmp_mv=interval[m+1]
              

            elif tmp_mv >=10:
                cnt += 1
                break
    print("#{} {}".format(i+1,cnt))    