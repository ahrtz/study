import copy

    


dr=[-1,1,0,0]
dc=[0,0,-1,1]

N,M = map(int,input().split())
pan=[]
for _ in range(N):
    pan.append(list(map(int,input().split())))
zero_list=[]
virus_list=[]
visited=[[0]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if pan[r][c]==0:
            zero_list.append((r,c))
        if pan[r][c]==2:
            virus_list.append((r,c))
## 이제 제로리스트 세개 뽑기 하고 1로 바꾸고 퍼뜨리면 댐 
combi=[]
max_cnt=0
for i in range(len(zero_list)-2):
    for j in range(i+1,len(zero_list)-1):
        for k in range(j+1,len(zero_list)):
            combi1=[]
            combi1.append(zero_list[i])
            combi1.append(zero_list[j])
            combi1.append(zero_list[k])
            combi.append(combi1)
# print("~")
while len(combi)!=0:
    wall = combi.pop()
    tmp_pan=copy.deepcopy(pan)
    for w in range(3):
        a1,b1 = wall[w]
        tmp_pan[a1][b1]=1
    ## 여기서 bfs 
    for v in range(len(virus_list)):
        sr,sc = virus_list[v]
        togo=[(sr,sc)]
        while togo !=[]:
            ssr,ssc = togo.pop()
            for a in range(4):
                newr= ssr + dr[a]
                newc = ssc + dc[a]
                if 0<=newr<N and 0<=newc<M and tmp_pan[newr][newc]==0:
                    togo.append((newr,newc))
                    tmp_pan[newr][newc]=2
    cnt=0
    for r in range(N):
        for c in range(M):
            if tmp_pan[r][c]==0:
                cnt+=1
    if max_cnt<cnt:
        max_cnt=cnt
print(max_cnt)