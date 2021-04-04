maze = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]

n=len(maze)
new_maze = [[1]*(n+2) for _ in range(n+2)]
for i in range(n):
    for j in range(n):
        new_maze[i+1][j+1]=maze[i][j]
print(new_maze)