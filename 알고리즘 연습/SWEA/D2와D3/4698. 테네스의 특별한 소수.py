def prime_list(n):
    
    sieve = [True] * n

    
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    
    return [i for i in range(2, n) if sieve[i] == True]
T=int(input())
sosu_list=prime_list(10**6)

for tc in range(T):
    D,A,B = map(int,input().split())
    res=[]
    for n in sosu_list:
        if A<=n<=B and str(D) in str(n):
            res.append(n)
    print("#{} {}".format(tc+1,len(res)))
        