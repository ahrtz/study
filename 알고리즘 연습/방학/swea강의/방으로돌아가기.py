T= int(input())
for tc in range(T):
    N= int(input())
    route = [0]*201
    for _ in range(N):
        start,end = map(int,input().split())
        if start>end: # 앞뒤 순서 바꾸기 크기 비교
            start,end = end,start
        if start %2 ==0:
            start -=1
        if end %2 == 0 :
            end -=1
        if start == end:
            route[start//2] += 1
        else:
            for i in range(start//2,(end//2)+1):
                route[i] += 1 
    print("#{} {}".format(tc+1,max(route)))

