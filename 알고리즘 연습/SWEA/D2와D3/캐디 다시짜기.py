import copy

N,M,D = map(int,input().split()) # row col 사거리
pan = []
for _ in range(N):
    tmp = list(map(int,input().split()))
    pan.append(tmp)



combi_list=[]
for i in range(M-2):
    goongsu=[0,0,0,0,0]    
    for j in range(i+1,M-1):
        for k in range(j+1,M):
            goongsu[i]=1
            goongsu[j]=1
            goongsu[k]=1
            combi_list.append(goongsu)
            goongsu=[0,0,0,0,0]
print(combi_list)
for baechi in goongsu:
    pan_copy = copy.deepcopy(pan)
    pan_copy.append(baechi)# 판에 깔았고 이제 검색
    for g_idx in range(M):
        for l in range(len(pan_copy)-1):
            