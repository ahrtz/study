import itertools
a,b = map(int,input().split())
if b ==1 :
    for k in range(1,a+1):
        print(k)
else:
    lis=list(itertools.permutations(range(1,a+1),b))
    for k in lis:
        print(" ".join(repr(l) for l in k))
