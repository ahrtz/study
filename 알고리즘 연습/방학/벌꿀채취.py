T=int(input())
for tc in range(T):
    N,M,C = map(int,input().split())
# print(pan)
pan = [list(map(int,input().split())) for _ in range(N)]
cnt1 = 0
cnt2 = 0
check = [[0]*N for _ in range(N)]
for r in range(N):
    for c in range(N-M):
        for i in range(M):
            check[r][c+i]=1
        
    for r1 in range(N):
        for c1 in range(N-M):
            if check[r1][c1]==0 and c1+(M-1)<N:
                # 나주에