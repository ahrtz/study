import sys
def is_prime(num):
    if(num <= 1):
        return False
    
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        
        i += 1
    return True
def prime_list(n):
 
    sieve = [True] * n

 
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n, i): 
                sieve[j] = False

    
    return [i for i in range(2, n) if sieve[i] == True]

n=int(sys.stdin.readline())
for i in range(n):
    a= int(sys.stdin.readline())
    half = len(prime_list(a))//2
    if is_prime(a/2) ==True:
        print(int(a/2),int(a/2))
    elif is_prime(a/2)== False :
        while is_prime(a-prime_list(a)[half]):
            half -=1

        print(min(a-prime_list(a)[half+1],prime_list(a)[half+1]),max(a-prime_list(a)[half+1],prime_list(a)[half+1]))

