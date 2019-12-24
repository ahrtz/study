def sosu(n):
    cnt = 0
    for i in range (1,n+1) :
        if n % i ==0:
            cnt += 1
    if cnt ==2 :
        return n 
    else:
        return 0
n= int(input())

a= input().split()
b=[]
result = []
for i in range(len(a)):
    b.append(int(a[i]))
for i in range(len(b)):
    result.append(sosu(b[i]))
c=[]
for i in range(len(result)):
    if result[i] > 0 : 
        c.append(result[i])
print(c)
print(result)
