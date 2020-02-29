import itertools,pprint,copy

def bomb(x,y):
    global pan1
    if pan1[x][y]==1:
        pan1[x][y]=0
    if pan1[x][y]>1:
        temp = pan1[x][y] 
        pan1[x][y] = 0
        for i in range(1,temp):
            for dir in range(4):
                x1 = x+d[dir][0]*i
                y1 = y+d[dir][1]*i
                if 0<=x1<W and 0<=y1<H:
                    if pan1[x1][y1]>0:
                        bomb(x1,y1)
                    
def check(a): #a는 열번호 
    for i in range(H):
        if pan1[i][a]!=0:
            break
    return i


T=int(input())
for tc in range(T):
    N,W,H = map(int,input().split()) # w 가 열 H가 행
    pan=[list(map(int,input().split()))  for _ in range(H)]
    # 가로 방향으로 판 바꾸기 
    N_list=list(range(W))
    # pan1=[]
    # for i in range(W):
    #     tmp=[]
    #     for k in range(H):
    #         tmp.append(pan[k][i])
    #     pan1.append(tmp)
    N_combi = list(itertools.combinations_with_replacement(N_list,N))
    d = ((0,-1),(1,0),(0,1),(-1,0))
    # print(N_combi[0])
    #아래로 깔아내리는 거 
    final=156216512
    for n in N_combi:
        pan1=copy.deepcopy(pan)
        cnt=0
        for i in range(N):
            tmp=n[i]
            r_num = check(tmp)
            bomb(r_num,tmp)
            for r in range(H-1,-1,-1):
                for c in range(W):
                    if pan1[r][c]==0 and 0<=(r-1):
                        if pan1[r-1][c]!=0:
                            pan1[r][c],pan1[r-1][c]=pan1[r-1][c],pan1[r][c]
        
        for fr in range(H):
            for fc in range(W):
                if pan1[fr][fc]!=0:
                    cnt += 1 
        if final > cnt:
            final = cnt
    print(final)
    # 필요한거 터뜨리는거랑 아래로 내리는거 그 행에서 0을 제외한 게 몇번째 행에 있는지 찾는거

