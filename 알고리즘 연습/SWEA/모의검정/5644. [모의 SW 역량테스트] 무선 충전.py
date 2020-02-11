
import pprint


T=int(input())
for tc in range(T):
    M,A = map(int,input().split())
    pan=[[0 for _ in range(10)] for _ in range(10)]
    A_route = list(map(int,input().split()))
    B_route = list(map(int,input().split()))
    Ap=[]
    
    for _ in range(A):
        tmp = list(map(int,input().split()))
        Ap.append(tmp)
    Ap_power=[] # 추후 같은 범위에 있는지 체크할때



    for x in Ap:
        Ap_power.append(x[3])
        for row in range(10):
            for col in range(10):
                if abs((x[1]-1)-row)+abs((x[0]-1)-col)<=x[2]:
                    print(row,col)
                    try:
                            pan[row][col]+=x[3]
                            
                    except :
                        pass
    
    d=[(0,0),(-1,0),(0,1),(1,0),(0,-1)]
    
    a=[0,0] # 시작점 좌표
    b=[10,10]
    a_tong=0
    b_tong=0
    for mv in range(len(M)):
        a_newx = a[0] + d[A_route[mv]]
        a_newy = a[1] + d[A_route[mv]]
        b_newx = b[0] + d[B_route[mv]]
        b_newy = b[1] + d[B_route[mv]]
        if (pan[a_newx][a_newy] or pan[b_newx][b_newy]) not in Ap_power:
            a_tong+=pan[a_newx][a_newy]
        
            
        