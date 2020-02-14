# def f():


n= 10
fibo = [0]*(n+1)
fibo[1]=1

for i in range(2,n+1):
    fibo[i] = fibo[i-1]+fibo[i-2]
print(fibo)

fact= [0]*(n+1)
fact[0] =1 
fact[1]= 1
for i in range(2,n+1):
    fact[i]= i * fact[i-1]%1000000007
    print(fact)