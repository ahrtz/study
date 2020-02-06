import pprint
T=int(input())
for tc in range(T):
    N,M = map(int,input().split())
    pan=[[0]*N for _ in range(N)]
    tmp=N//2
    pan[tmp][tmp] = 2
    pan[tmp-1][tmp-1] = 2
    pan[tmp-1][tmp] = 1
    pan[tmp][tmp-1] = 1
    # black=[(tmp,tmp-1),(tmp-1,tmp)] # 1
    # white=[(tmp,tmp),(tmp-1,tmp-1)] # 2

    # dcol=[-1,1,0,0]
    # drow=[0,0,-1,1]
    

    for k in range (M):
        row,col,color = map(int,input().split())
        rrow = row - 1
        ccol = col - 1
        pan[rrow][ccol] = color
        # 검사하기 가로먼저 세로
        while True:
            
            # 가로 ->
            new_col = ccol + 1
            if 0 <= new_col < N and pan[rrow][new_col]!=color and pan[rrow][new_col]!=0:
                ccol = new_col
            elif 0 <= new_col < N and pan[rrow][new_col] == 0:
                break
            elif 0<= new_col < N and pan[rrow][new_col]==color:
                tmpcol=new_col
                for tttt in range(ccol,tmpcol,1):
                    pan[rrow][tttt]=color
                break
            if new_col>=N:
                break
        rrow = row - 1
        ccol = col - 1
        while True:
            # 가로 <-
            
            new_col = ccol - 1
            if 0 <= new_col < N and pan[rrow][new_col]!=color and pan[rrow][new_col]!=0:
                ccol = new_col
            if 0 <= new_col < N and pan[rrow][new_col] == 0:
                break
            if 0<= new_col < N and pan[rrow][new_col]==color:
                tmpcol=new_col
                for tttt in range(tmpcol,col-1,1):
                    pan[rrow][tttt]=color
                break
            if new_col<0:
                break
        rrow = row - 1
        ccol = col - 1
        while True:
            # 위쪽
            
            new_row = rrow - 1
            
            if 0 <= new_row < N and pan[new_row][ccol]!=color and pan[new_row][ccol]!=0:
                rrow = new_row
            if 0 <= new_row < N and pan[new_row][ccol] == 0:
                break
            if 0<= new_row < N and pan[new_row][ccol]==color:
                tmprow=new_row
                for tttt in range(tmprow,row-1,1):
                    pan[tttt][ccol]=color
                break
            if new_row<0:
                break
        rrow = row - 1
        ccol = col - 1
        while True:
            
            # 아래쪽
            new_row = rrow + 1
            if 0 <= new_row < N and pan[new_row][ccol]!=color and pan[new_row][ccol]!=0:
                rrow = new_row
            if 0 <= new_row < N and pan[new_row][ccol] == 0:
                break
            if 0<= new_row < N and pan[new_row][ccol]==color:
                tmprow=new_row
                for tttt in range(row-1,tmprow,1):
                    pan[tttt][ccol]=color
                break
            if new_row>=N:
                break
        rrow = row - 1
        ccol = col - 1
        while True:
            # 대각 위 ->
            
            new_row = rrow -1
            new_col = ccol + 1
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col]!=color and pan[new_row][new_col]!=0:
                ccol = new_col
                rrow = new_row
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col] == 0:
                break
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col]==color:
                tmpcol = new_col
                tmprow = new_row
                for tttt in range(0,tmpcol-ccol):
                    pan[rrow-tttt][ccol+tttt]=color
                break
            if new_row<0 or new_col>=N:
                break
        rrow = row - 1
        ccol = col - 1
        while True:
            # 대각 아래 ->
            new_row = rrow + 1
            new_col = ccol + 1
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col]!=color and pan[new_row][new_col]!=0:
                ccol = new_col
                rrow = new_row
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col] == 0:
                break
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col]==color:
                tmpcol = new_col
                tmprow = new_row
                for tttt in range(0,tmpcol-ccol):
                    pan[rrow+tttt][ccol+tttt]=color
                break
            if new_row>=N or new_col >=N:
                break
        rrow = row - 1
        ccol = col - 1
        while True:
            # 대각 위 <-
            new_row = rrow - 1
            new_col = ccol - 1
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col]!=color and pan[new_row][new_col]!=0:
                ccol = new_col
                rrow = new_row
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col] == 0:
                break
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col]==color:
                tmpcol = new_col
                tmprow = new_row
                for tttt in range(0,ccol-tmpcol):
                    pan[rrow-tttt][ccol-tttt]=color
                break
            if new_row<0 or new_col<0:
                break
        rrow = row - 1
        ccol = col - 1
        while True:
            # 대각 아래 <-
            new_row = rrow + 1
            new_col = ccol - 1
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col]!=color and pan[new_row][new_col]!=0:
                ccol = new_col
                rrow = new_row
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col] == 0:
                break
            if 0 <= new_col < N and 0 <= new_row < N and pan[new_row][new_col]==color:
                tmpcol = new_col
                tmprow = new_row
                for tttt in range(0,ccol-tmpcol):
                    pan[rrow+tttt][ccol-tttt]=color
                break
            if new_row>=N or new_col<0:
                break
    w_cnt=0
    b_cnt=0
    for i in range(len(pan)):
        b_cnt+=pan[i].count(1)
        w_cnt+=pan[i].count(2)
    pprint.pprint(pan)
    print("#{} {} {}".format(tc+1,b_cnt,w_cnt))
        


                

