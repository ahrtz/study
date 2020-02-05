import itertools
n,m,d = map(int,input().split())
castle = []
n_list=[1]*3+[0]*(n-3)
tmp_list=set(itertools.permutations(n_list))
print(tmp_list)
# for i in range(n):
#     tmp = list(map(int,input().split()))
#     castle.append(tmp)
