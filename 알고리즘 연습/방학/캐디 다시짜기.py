import copy
n,m,d = map(int,input().split())
castle = []
#궁수 조합짜기
combi_list=[]
for i in range(m-2):
    goongsu=[0]*m   
    for j in range(i+1,m-1):
        for k in range(j+1,m):
            goongsu[i]=1
            goongsu[j]=1
            goongsu[k]=1
            combi_list.append(goongsu)
            goongsu=[0]*m

for _ in range(n):
    tmp = list(map(int,input().split()))
    castle.append(tmp)
result=[]

for goongsu1 in combi_list:
    castle1 = copy.deepcopy(castle)
    castle1.append(goongsu1)
    cnt=0
    while len(castle1) !=1:
        for i in range(m):
            attack_list=[]
            if castle1[-1][i]==1:# 궁수위치 확인
                for r in range(len(castle1)-2,-1,-1):
                    for c in range(m):
                        if abs(len(castle1)-1-r)+abs(i-c)<=d and castle1[r][c]>=1:
                            attack_list.append((r,c,abs(len(castle1)-1-r)+abs(i-c)))
                            #궁수가 공격할수 있는 적들에 대한 리스트
                            # 여러명이 하나 때릴 수 있으니까 1이상
            # 한명의 궁수에 대해 만들어진 어택리스트 에서 가장 왼쪽걸 뽑자 
                if len(attack_list)==1:#한개면 그냥 그거 더하기 1 
                    castle1[attack_list[0][0]][attack_list[0][1]] += 1
            # 여러개 있을때 
        #이제 어택리스트에서 가장 가깝고 왼쪽에 있는거 거리 정렬 한후 컬럼 정렬
                if len(attack_list)>1:
                    attack_list=sorted(attack_list,key= lambda x:(x[2],x[1]))
                    castle1[attack_list[0][0]][attack_list[0][1]] += 1 
        


        # 이제 1 초과하는것들 세서 카운트 추가하고 kill 하고 한줄삭제
        for row in range(len(castle1)):
            for col in range(m):
                if castle1[row][col] >1:
                    cnt+=1
                    castle1[row][col]=0
        castle1.remove(castle1[-2])
        attack_list=[]
    result.append(cnt)
print(max(result))