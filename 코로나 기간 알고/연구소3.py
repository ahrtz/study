## 틀림 
import copy,pprint

dr=[-1,1,0,0]
dc=[0,0,-1,1]

N,M = map(int,input().split())
pan=[]
for _ in range(N):
    pan.append(list(map(int,input().split())))
virus=[]
visited=[[0]*N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if pan[r][c]==1:
            pan[r][c]='/'
        if pan[r][c]==2:
            pan[r][c]='*'
            virus.append((r,c))
## 꽉차면 돌릴필요도 없는거 여기서
flag1=0
for r in range(N):
    
    if set(pan[r])=={'*','/'} or set(pan[r])=={'*'} or set(pan[r])=={'/'}:
        flag1+=1


if flag1!=N:
    # * 중에 M개 뽑아야댐
    # 조합 함수 
    check_list = [False] * len(virus)
    arr = []
    virus_list = []
    def dfs(cnt):
        global virus_list
        if(cnt == M):
            a=arr[:]
            virus_list.append(a)
            return
        for i in range(0, len(virus)):
            if(check_list[i]):
                continue
            check_list[i] = True
            arr.append(virus[i])
            dfs(cnt + 1)
            arr.pop()
            for j in range(i + 1, len(virus)):
                check_list[j] = False
    dfs(0)


    ###############

    flag = 0
    max_cnt=1111111111
    for i in range(len(virus_list)):
        tmp_pan = copy.deepcopy(pan)
        tmp_virus = virus_list[i]
        # 요 아래에서 시작
        togo=[]
        cnt=0
        for k in range(len(tmp_virus)):
            sr,sc = tmp_virus[k]
        # 초기 값 주기
            for t in range(4):
                newr = sr + dr[t]
                newc = sc + dc[t]
                if 0<=newr<N and 0<=newc<N and (tmp_pan[newr][newc]==0 or tmp_pan[newr][newc]=='*'):
                    tmp_pan[newr][newc]=1
                    togo.append((newr,newc))
        #bfs 돌리기 
        while togo!=[]:
            sr,sc = togo.pop(0)
            for t in range(4):
                newr = sr + dr[t]
                newc = sc + dc[t]
                if 0<=newr<N and 0<=newc<N and (tmp_pan[newr][newc]==0 or tmp_pan[newr][newc]=='*'):
                    tmp_pan[newr][newc]=tmp_pan[sr][sc]+1
                    togo.append((newr,newc))
                    if cnt<tmp_pan[newr][newc]:
                        cnt=tmp_pan[newr][newc]
                        
        # 점검하기 
        print(cnt,"%")
        pprint.pprint(tmp_pan)
        for r in range(N):
            if 0 in tmp_pan[r]:
                flag+=1
                break
        else:
            if max_cnt>cnt:
                max_cnt=cnt

    if flag == len(virus_list):
        print(-1)
    else:
        print(max_cnt)    
else:
    print(0)