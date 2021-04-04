def solution(N):
    tmp=[0]*50
    tmp[1]=1
    tmp[2]=2
    for i in range(3,50):
        tmp[i]=tmp[i-1]+tmp[i-2]
    
    return tmp[N]