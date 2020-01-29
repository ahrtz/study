Tc=int(input())
for tc in range(1,Tc):
    a=int(input())
    result = [[0]*a (for _ in range(a))]
    #짝수일때
    if a%2==0:
        for i in range(a):
            for k in range(a):
    

    #홀수일때
    else:
        for k in range(a):
            result[0][k]=k+1
        for i in range(a):
            result[a-1][i]= a-1 + i + 1
        for i in range(a-1,-1,-1):
            result[i][a-1] = a**2-i-(a-1)
        