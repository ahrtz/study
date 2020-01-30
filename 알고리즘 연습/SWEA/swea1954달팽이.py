
    

        



Tc=int(input())
for tc in range(1,Tc+1):
    a=int(input())
    result = [[0]*a for _ in range(a)]
    

    row = 0
    col = 0
    row_diff = 0
    col_diff = 1
    num = 1 #들어갈 숫자 
    visit = [[0]*a for _ in range(a)] # 방문했던 곳인지 체크 
    visited=[]
    while True:
        result[row][col]=num
        visit[row][col]=1
        visited.append([row,col]) # 함수용
        
        num += 1
        row += row_diff
        col += col_diff 
       
        
        if len(visited)==a**2:
            break
        if row > a-1 or col > a-1 or row < 0 or col < 0 or [row,col] in visited :

            if visited[-1][1] > visited[-2][1]: #내려가기
                col -= 1
                row += 1
                row_diff = 1
                col_diff = 0
                
            if visited[-1][1] < visited[-2][1]: # 올라오기
                row -= 1
                col += 1
                row_diff = -1
                col_diff = 0
                
            if visited[-1][0] > visited[-2][0]: #좌측가기
                col -= 1
                row -= 1
                row_diff = 0
                col_diff = -1
            
            if visited[-1][0] < visited[-2][0]: # 우측가기
                col += 1
                row += 1
                row_diff = 0
                col_diff = 1       
                
    print("#{}".format(tc))            
    for line in result:
        print(" ".join(str(j)for j in line))

        # print(" ".join(result[i]))








    # if row > a-1  :
        #     row -= 1
        #     turn()
        
        # if  col >a-1 or visit[row][col]==0:
        #     col -= 1
        #     turn()
        
        # if  row<0  or visit[row][col]==0:
        #     row += 1
        #     turn()
        
        # if  col < 0 or visit[row][col]==0:
        #     turn()
        
        # if row > a-1 or col >a-1 or row<0 or col < 0 or visit[row][col]==0:
        #     turn()
        
        # if row > a-1 or col >a-1 or row<0 or col < 0 or visit[row][col]==0:
        #     turn()