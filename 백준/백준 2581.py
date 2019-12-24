def sosu(n):
    cnt = 0
    for i in range (1,n+1) :
        if n % i ==0:
            cnt += 1
    if cnt ==2 :
        return n 
    else:
        return 0

a=[]
start = int(input())
end= int(input())
result = []
c=[]
for i in range(start,end+1):
    a.append(i)
for i in range(len(a)):
    result.append(sosu(a[i]))
for i in range(len(result)):
    if result[i] > 0 : 
        c.append(result[i])
if len(c)>0:
    print(sum(c))
    print(min(c))
else:
    print(-1)
