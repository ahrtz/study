T=int(input())
for tc in range(T):
    N,M,C = map(int,input().split()) # N : 가로길이 M : 벌통크기 c: 벌통용량
# print(pan)
pan = [list(map(int,input().split())) for _ in range(N)]
cnt1 = 0
cnt2 = 0
check = [[0]*N for _ in range(N)]

for r in range(N):
    contain1=[]
    contain2=[]
    for c in range(N-M):
        for r1 in range(N):
            for c1 in range(N-M):
                if r==r1 and ((c+M)>c1 or (c-M)<c1):
                    continue
                for k in range(M):
                    contain1.append(pan[r][c+k])

#뭐르겟어요