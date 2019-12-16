def room_num(N):
    if N%H==0:
        first_num = H
        later_num = N//H
    else:
        first_num=N % H
        later_num=N//H +1
    
    return print(str(first_num)+str("%02d"%later_num))
            
num = int(input())
for i in range(num):
    H,W,N=map(int,input().split())
    room_num(N)
