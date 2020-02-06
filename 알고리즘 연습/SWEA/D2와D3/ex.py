import itertools
n,m,d = 5,5,1
castle = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]]
n_list=[1]*3+[0]*(n-3)
tmp_list=set(itertools.permutations(n_list))

# for i in range(n):
#     tmp = list(map(int,input().split()))
#     castle.append(tmp)
for i in range(len(tmp_list)):
    castle.insert(0,tmp_list[i])
    # 궁수 배치 배열