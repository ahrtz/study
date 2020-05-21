from collections import deque
T=int(input())
visited=[0]*(1000001)
for tc in range(T):
    N,M= map(int,input().split())
    cnt=0
    Q=deque()
    Q.append((N,cnt))
    visited[N]=(tc+1)
    result =0
    while Q:
        num,cnt = Q.popleft()
        if num==M:
            result = cnt
            break
        for i in range(4):
            if i==0:
                res=num+1
                if 0<res<=10**6 and visited[res]!=(tc+1):
                    visited[res]=(tc+1)
                    Q.append((res,cnt+1))
            elif i==1:
                res=num-1
                if 0<res<=10**6 and visited[res]!=(tc+1):
                    visited[res]=(tc+1)
                    Q.append((res,cnt+1))
            elif i==2:
                res=num*2
                if 0<res<=10**6 and visited[res]!=(tc+1):
                    visited[res]=(tc+1)
                    Q.append((res,cnt+1))
            elif i==3:
                res=num-10
                if 0<res<=10**6 and visited[res]!=(tc+1):
                    visited[res]=(tc+1)
                    Q.append((res,cnt+1))
        # print(Q)


    print(f"#{tc+1} {result}")
    