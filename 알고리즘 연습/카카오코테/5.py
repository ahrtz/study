def solution(n, s, a, b, fares):
    inf=int(1e10)
    fee_graph=[[inf]*(n) for _ in range(n)]
    for i in range(n):
        fee_graph[i][i]=0

    for log in fares:
        sp,ed,fare = log
        fee_graph[sp-1][ed-1]=fare
        fee_graph[ed-1][sp-1]=fare
    
    for t in range(n):
        for i in range(n):
            for j in range(i,n):
                if i!=j:
                    temp = min(fee_graph[i][j], fee_graph[i][t] + fee_graph[t][j]) 
                    fee_graph[i][j]=temp
                    fee_graph[j][i]=temp

    minval=inf
    for t in range(n):
        minval=min(fee_graph[s-1][t]+fee_graph[t][a-1]+fee_graph[t][b-1],minval)

    # print(fee_graph)
    # print(minval)
    return minval


n=6
s=	4
a=	6
b=	2
fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

solution(n,s,a,b,fares)