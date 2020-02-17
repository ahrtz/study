T=int(input())
for tc in range(T):
    N=int(input())
    farm=[list(map(int,input())) for _ in range(N)]
    cnt=0
    for r in range(N):
        for c in range(N):
            if abs(N//2-r)+abs(N//2-c)<=N//2:
                cnt+= farm[r][c]
    print("#{} {}".format(tc+1,cnt))