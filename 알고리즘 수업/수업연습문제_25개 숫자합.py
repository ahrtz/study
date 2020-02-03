import random
a= list(range(1,26))
random.shuffle(a)

pann = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        pann[i][j]= a.pop()
print(pann)
## 랜덤 판을 구하기 

dx=[-1,1,0,0] # 난 이게 열 위 아래 
dy=[0,0,-1,1] # 난 이게 행 좌 우 
res=0
for i in range(5):
    for j in range(5):
        summ=0
        for k in range(4):
            newx= i + dx[k]
            newy= j + dy[k]
            if 0<=newx<5 and 0<=newy<5:
                summ += abs(pann[i][j]- pann[newx][newy])
        res+=summ

print(res)