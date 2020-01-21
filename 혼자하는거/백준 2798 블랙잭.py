a,max = map(int,input().split())

num = list(map(int,input().split(" ")))
cnt = 0
for i in range(a-2):
    for j in range(i+1,a-1):
        for k in range(j+1,a):
            suma = num[i]+num[j]+num[k]
            if suma<=max:
                if suma>cnt:
                    cnt = suma
print(cnt)

