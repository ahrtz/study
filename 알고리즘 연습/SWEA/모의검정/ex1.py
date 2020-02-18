def dfs(sp, visited, miro):
    global ans
    visited.add(sp)
    si, sj = sp[0], sp[1]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for k in range(4):
        ni = si + dx[k]
        nj = sj + dy[k]
        if (ni, nj) not in visited:
            if miro[ni][nj] == '3':
                ans = 1
                return 1
            elif miro[ni][nj] == '0':
                if dfs((ni, nj), visited, miro) == 1:
                    return 1
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 주변을 벽으로 둘러싼 미로 만들기
    maze = [['1']+list(input())+['1'] for _ in range(n)]
    maze.insert(0,['1']*(n+2))
    maze.append(['1']*(n+2))
    visited = set([])
    for i in range(n+1,-1,-1):
        for j in range(n+1,-1,-1):
            if maze[i][j] == '2':
                start = (i,j)
                break
    ans =0
    dfs(start,visited,maze)
    print('#{} {}'.format(tc, ans))
    # for line in maze:
    #     print(line)