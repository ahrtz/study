import itertools

a=[6,7,8]
# 꿀통 13 
for i in range(1,len(a)+1):
    b=list(itertools.combinations(a,i))
    for m in b:
        print(sum(m))