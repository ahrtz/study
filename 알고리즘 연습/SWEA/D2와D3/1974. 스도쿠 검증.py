


T=int(input())
for tc in range(T):
    puzzle=[]
    for _ in range(9):
        tmp = list(map(int,input().split()))
        puzzle.append(tmp)
    garo_sum=[]
    for row in range(9): # 가로 검증
        garo_sum.append(sum(puzzle[row]))
    
    sero_sum=[]
    for col in range(9): # 세로 검증
        a = 0
        for row in range(9):
           a += puzzle[row][col]
        sero_sum.append(a)
    sagak_sum=[]
    for i in range(2):
        
        for k in range(2):
            b = 0
            b += puzzle[1+3*i][1+3*k]
            b += puzzle[1+3*i][1+3*k-1]
            b += puzzle[1+3*i+1][1+3*k-1]
            b += puzzle[1+3*i+1][1+3*k]
            b += puzzle[1+3*i+1][1+3*k+1]
            b += puzzle[1+3*i][1+3*k+1]
            b += puzzle[1+3*i-1][1+3*k+1]
            b += puzzle[1+3*i-1][1+3*k]
            b += puzzle[1+3*i-1][1+3*k-1]
        sagak_sum.append(b)
    print(garo_sum,sero_sum,sagak_sum)