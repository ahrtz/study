   
n=123456
sieve = [True] * n
m = int(n ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:           
        for j in range(i+i, n, i): 
            sieve[j] = False

result = [i for i in range(2, n) if sieve[i] == True]

while True :
    a=int(input())
    if a == 0:
        break
    cnt = 0
    for i in result:
        if i <= a :
            continue
        elif a * 2 >= i > a:
            cnt += 1
        else:
            break
    print(cnt)
