import itertools

t= int(input())
for i in range(t):
    N,K = map(int,input().split())
    itm=[]
    for k in range(N):
        V,C=map(int,input().split())
        
        itm.append((V,C))
    
    a=itertools.combinations(itm,2)
    print(list(a))