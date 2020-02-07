T=int(input())
for tc in range(T):
    N,M,K,H = map(int,input().split())
    pan=[]
    cnt=0
    delta = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
    for i in range(N):
        pan.append(list(map(int,input().split())))
    for row in range(1,N-1):
        for col in range(1,M-1):
            num_list=[]
            for check in range(8):
                dx,dy = delta[check]
                nx=row+dx
                ny=col+dy
                num_list.append(pan[nx][ny])
            if max(num_list)-min(num_list)<=K and pan[row][col]>= min(num_list) and pan[row][col]-min(num_list)<=H:
                cnt+=1
    # if cnt == 0:
    #     print("#{} {}".format(tc+1,0))
    else:
        print("#{} {}".format(tc+1,cnt))
    
    
 
 