a=[3,3,3,3,3,3,3]
for _ in range(2):
    a[a.index(3)]=1
    print(a.index(3))
    print(a)