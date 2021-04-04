def isPrime(n):
    # Write your code here
    # candidate=list(range(1,n**(1/2)))
    for i in range(2,int(n**(1/2))+1):
        print(int(n**(1/2))+1)
        if n%i==0:
            return i
    return 1
            
isPrime(4)