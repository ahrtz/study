down=[1,0]
right=[0,1]
up=[-1,0]
left=[0,-1]
direction = {'down':down,'right':right,'up':up,'left':left}
def solution(maze):
    global direction
    sp = [0,0]
    goal= (len(maze),len(maze))
    if maze[0][1]==1: # 초기 방향 설정
        dirr = 'down'
        
    else:
        dirr='right'
    cnt=0
    n=len(maze)
    new_maze = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_maze[i+1][j+1]=maze[i][j]
    maze= new_maze
    sp=[1,1]
    while sp != goal:
        
        newsp_x = sp[0]+direction[dirr][0]
        newsp_y = sp[1]+direction[dirr][1]
        # print(newsp_x,newsp_y,cnt)
        
        if maze[newsp_x][newsp_y]==1: # 벽 부딛히면 오른쪽회전 
            if dirr =='down':
                dirr = 'left'
            elif dirr == 'right':
                dirr = 'down'
            elif dirr == 'up':
                dirr = 'right'
            elif dirr =='left':
                dirr = 'up'
        elif maze[newsp_x][newsp_y]==0: 
            cnt+=1
            if dirr=='down' and maze[newsp_x][newsp_y+1]==1:
                sp[0]=newsp_x
                sp[1]=newsp_y
            elif dirr=='down' and maze[newsp_x][newsp_y+1]==0: # 좌횟전
                sp[0]=newsp_x
                sp[1]=newsp_y
                dirr = 'right'
            elif dirr == 'right' and maze[newsp_x-1][newsp_y]==1: # 계속 진행
                sp[0]=newsp_x
                sp[1]=newsp_y
            elif dirr == 'right' and maze[newsp_x-1][newsp_y]==0:
                sp[0]=newsp_x
                sp[1]=newsp_y
                dirr = 'up'
            elif dirr == 'up' and maze[newsp_x][newsp_y-1]==1: # 계속 진행
                sp[0]=newsp_x
                sp[1]=newsp_y
            elif dirr == 'up' and maze[newsp_x][newsp_y-1]==0:
                sp[0]=newsp_x
                sp[1]=newsp_y
                dirr = 'left'
            elif dirr == 'left' and maze[newsp_x+1][newsp_y]==1: # 계속 진행
                sp[0]=newsp_x
                sp[1]=newsp_y
            elif dirr == 'left' and maze[newsp_x+1][newsp_y]==0:
                sp[0]=newsp_x
                sp[1]=newsp_y
                dirr = 'down'
            if sp[0]==goal[0] and sp[1]==goal[1]:
                break
            
    return cnt

maze = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]
print(solution(maze))
