import copy
n,m,d = map(int,input().split())
castle = []
# n_list=[1]*3+[0]*(m-3)
# tmp_list=list(set(itertools.permutations(n_list)))
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
    # print(len(castle1),n)
    while len(castle1) !=1:
        for i in range(m):
            attack_list=[]
            if castle1[-1][i]==1:# 궁수위치 확인
                for r in range(len(castle1)-2,-1,-1):
                    # print(len(castle1),"^") 
                    for c in range(m):
                        if abs(len(castle1)-1-r)+abs(i-c)<=d and castle1[r][c]>=1:
                            # print("#")
                            attack_list.append((r,c,abs(len(castle1)-1-r)+abs(i-c)))
                            # print(r,c)
                    # if len(attack_list)!=0:
                    #     break
            # 한명의 궁수에 대해 만들어진 어택리스트 에서 가장 왼쪽걸 뽑자 
                if len(attack_list)==1:
                    castle1[attack_list[0][0]][attack_list[0][1]] += 1
            # 여러개 있을때 
        #이제 어택리스트에서 가장 가깝고 왼쪽에 있는거 
                if len(attack_list)>1:
                    attack_list=sorted(attack_list,key= lambda x:(x[2],x[1]))
            #         # tmpp.append(attack_list[0])
                    castle1[attack_list[0][0]][attack_list[0][1]] += 1 
        
            # for at in range(len(attack_list)):
            #     castle1[attack_list[at][0]][attack_list[at][1]] += 1


        # 이제 1 초과하는것들 세서 카운트 추가하고 한줄삭제
        for row in range(len(castle1)):
            for col in range(m):
                if castle1[row][col] >1:
                    cnt+=1
                    castle1[row][col]=0
        castle1.pop(-2)
        attack_list=[]
    result.append(cnt)
print(max(result))
    # print(goongsu)
    # print(attack_list)

