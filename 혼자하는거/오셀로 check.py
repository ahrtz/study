# test case의 수

delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
# 8방향 탐색을 위해 delta 선언
T= int(input())
for t_case in range(T):
    n, m = map(int, input().split())
    pan = [[0] * n for _ in range(n)]
    # 입력받기
    
    
    mid = n // 2
    # mid는 현재 보드 크기 n의 절반이다.
    
    
    pan[mid][mid] = 2
    pan[mid-1][mid-1] = 2
    pan[mid-1][mid] = 1
    pan[mid][mid-1] = 1
    # 초기화. 처음에 보드의 상태를 정의한다. 정중앙에 네 개의 돌이 엇갈려 놓여있다.
    
    
    for i in range(m):
        x, y, c = map(int, input().split())
        # 각각 보드위의 행, 열, 색을 저장한다.
        y, x = y-1, x-1
        # 문제의 좌표 표기가 1부터이므로 -1을 해준다.
        
        
        reverse = [] # 뒤집어야 할 돌을 저장할 리스트 reverse 초기화
        pan[x][y] = c
        # 8방향 탐색
        for i in range(8):
            dx, dy = delta[i]
            nx, ny = x + dx, y + dy
            while True:
                if nx < 0 or ny < 0 or nx > n-1 or ny > n-1: # 모서리인가?
                    reverse = []
                    break
                if pan[nx][ny] == 0: # 빈 칸을 만난경우 reverse를 초기화
                    reverse = [] 
                    break
                if pan[nx][ny]==c: # 같은 색을 만났으므로 break
                    break
                else: # 조건에 부합하는 돌을 reverse에 추가한다.
                    reverse.append((nx,ny))
                nx, ny = nx + dx, ny + dy
            for rx, ry in reverse: # 뒤집어준다.
                if c == 1:
                    pan[rx][ry] = 1
                else:
                    pan[rx][ry] = 2
        
    # 각각의 돌 숫자를 세준다.
    w, b = 0, 0
    for i in range(n):
        for j in range(n):
            if pan[i][j] == 1:
                w += 1
            elif pan[i][j] == 2:
                b += 1
     
    print('#{} {} {}'.format(t_case+1 ,w ,b))