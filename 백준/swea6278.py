a= int(input())
result = []
for i in range(1,a+1):
    if a % i == 0:
        result.append(i)
print(result)