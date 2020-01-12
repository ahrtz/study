result = []

for i in range(2,10):
    a=[]
    for k in range(1,10):
        if i * k % 3 ==0:
            pass
        elif i* k % 7 == 0 :
            pass
        else:
            a.append(i*k)
    result.append(a)
print(result)