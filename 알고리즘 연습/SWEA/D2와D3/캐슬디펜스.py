import itertools,copy
n,m,d = map(int,input().split())
castle = []
n_list=[1]*3+[0]*(m-3)
tmp_list=list(set(itertools.permutations(n_list)))

for i in range(n):
    tmp = list(map(int,input().split()))
    castle.append(tmp)
result=[]
castle1 = copy.deepcopy(castle)
for goongsu in tmp_list:
    castle1.append(goongsu)
    cnt=0
    # print(castle1)
    print(len(castle1),n)
    while len(castle1) !=1:
        attack_list=[]
        for i in range(m):
            if castle1[-1][i]==1:# 궁수위치 확인
                for r in range(len(castle1)-1):
                    print(len(castle1),"^") 
                    for c in range(m):
                        # print(r,c)
                        if abs(len(castle1)-1-r)+abs(i-c)<=d and castle1[r][c]==1:
                            # print("#")
                            attack_list.append((r,c,abs(len(castle1)-1-r)+abs(i-c)))
            #한명의 궁수에 대해 만들어진 어택리스트
            if len(attack_list)==1:
                castle1[attack_list[0][0]][attack_list[0][1]] += 1
            elif len(attack_list)>1:
                attack_list=sorted(attack_list,key= lambda x:(x[2],x[0]))
                
                castle1[attack_list[0][0]][attack_list[0][1]] += 1 
              
        else:
            pass 
            # 여러개 있을때 
        #이제 어택리스트에서 가장 가깝고 왼쪽에 있는거 
        # 이제 1 초과하는것들 세서 카운트 추가하고 한줄삭제
        for row in range(len(castle1)):
            for col in range(m):
                if castle1[row][col] >1:
                    cnt+=1
        result.append(cnt)
        castle1.remove(castle1[-2])
        attack_list=[]
print(result)
    # print(goongsu)
    # print(attack_list)

