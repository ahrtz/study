from itertools import combinations
from copy import deepcopy
import pprint
N,M = map(int,input().split())
pan=[]
for _ in range(N):
    pan.append(list(input().split()))
virus=[]
for r in range(N):
    print(r)
    for c in range(N):
        if pan[r][c]=='1':
            pan[r][c]='/'
        if pan[r][c]=='2':
            virus.append((r,c))
            pan[r][c]='*'
        if pan[r][c]=='0':
            pan[r][c]='$'
flag1=0
print(pan)
for r in range(N):
    if set(pan[r])=={'*','/'} or set(pan[r])=={'*'} or set(pan[r])=={'/'}:
        
        flag1+=1
if flag1 != N:
    virus_list = combinations(virus,M)
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]
    max_cnt=1000000000
    flag=0
    for vi in virus_list:
        tmp_pan=deepcopy(pan)
        togo=[]
        cnt=0
        check0=0
        for i in vi:
            rv,cv = i[0],i[1]
            togo.append((rv,cv))
            tmp_pan[rv][cv]=1
        ## 여기서부터 돌자
        while togo!=[]:
            sr,sc = togo.pop(0)
            for t in range(4):
                newr = sr + dr[t]
                newc = sc + dc[t]
                if 0<=newr<N and 0<=newc<N and (tmp_pan[newr][newc]=='$' or tmp_pan[newr][newc]=='*'):
                    tmp_pan[newr][newc]=tmp_pan[sr][sc]+1
                    togo.append((newr,newc))
                    if cnt<tmp_pan[newr][newc]:
                        cnt=tmp_pan[newr][newc]
        
        print(cnt,"%")
        pprint.pprint(tmp_pan)
        # 여기서 판은 다 만듬
        for r in range(N):
            if 0 in tmp_pan[r]:
                flag+=1
                check0+=1
                break
                
        if check0==0:
            if max_cnt>cnt:
                max_cnt=cnt

    if flag == len(list(virus_list)):
        print(-1)
    else:
        # print(cnt,"%")
        # pprint.pprint(tmp_pan)
        print(max_cnt)    
else:
    print(0)