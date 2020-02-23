import copy
pipe = {
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((-1, 0), (0, -1))
}


T=int(input())
for tc in range(T):
    n,m,r,c,l = map(int,input().split()) # n 세로 m 가로 pan  맨홀이 위치한 행과 열 , l 은 지나간 시간 
    pan =[]
    for _ in range(n):
        pan.append(list(map(int,input().split())))
    # count_pan = copy.deepcopy(pan)
    cnt=1 #맨처음 들어가는 위치
    sr,sc = r,c
    visited = [[0]*m for _ in range(n)]
    visited[r][c] = 1
    togo=[(r,c)]
    while togo:
        sr,sc = togo.pop(0)
        for dr,dc in pipe[pan[sr][sc]]:
            newr = sr + dr
            newc = sc + dc
            if 0<=newr<n and 0<=newc < m and not (visited[newr][newc] and pan[newr][newc]):
                if (-dr,-dc) in pipe[pan[newr][newc]]:
                    visited[newr][newc] += visited[sr][sc]+1
                    togo.append((newr,newc))
                    if visited[newr][newc] <= l:
                        cnt += 1
    print("#{} {}".format(tc+1,cnt))
        
    