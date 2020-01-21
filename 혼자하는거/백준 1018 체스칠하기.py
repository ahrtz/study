l,h= map(int,input().split())

chess_mom=[]
for j in range(h):
    chess_mom.append(input())
cnt=0
for i in range(len(chess_mom[0])-1):
    for j in range(len(chess_mom[0])-1):
        if chess_mom[i][j]==chess_mom[i+1][j] and chess_mom[i][j]==chess_mom[i][j+1] and chess_mom[i][j]==chess_mom[i-1][j] and chess_mom[i][j]==chess_mom[i][j-1]:
            cnt+=1
