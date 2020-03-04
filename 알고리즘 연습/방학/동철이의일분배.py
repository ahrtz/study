def calc(n, per):
    global max_per
    if per <= max_per:
        return
    if n == N:
        max_per = per
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            calc(n+1, per*num_list[n][i]/100)
            visited[i] = 0
T = int(input())
for tc in range(T):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    max_per = 0
    visited = [0] * N
    calc(0, 1)
    print('#{} {:6f}'.format(tc+1, max_per * 100))