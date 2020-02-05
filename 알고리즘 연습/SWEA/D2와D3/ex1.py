import itertools
n,m,d = 5,5,1
castle = [[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]]

# for i in range(n):
#     tmp = list(map(int,input().split()))
#     castle.append(tmp)

# 궁수 배치 배열했다 치고
print(castle[0].count(1))
a=castle[0].index(1)
print(castle[0].index(1,a+1))

# for i in range(n):#행단위 시작
    #궁수좌표 받아오기 
    
