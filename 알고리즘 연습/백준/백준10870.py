# def fibo(n):
#     if n ==0:
#         return 0 
#     if 1 <= n <3:
#         return 1
#     else:
#         return fibo(n-1)+ fibo(n-2)

# a= int(input())
# print(fibo(a))

#### ---------------- 2447 
# n=["***",'* *','***']

# def frac(k):
#     a=[]
#     for i in range(len(k) % 3):
#         a.append("{}\n{}\n{}".format(n[0],n[1],n[2]))
#         return a

# print(frac(9))
def stars(n):
    matrix=[]
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

star = ["***","* *","***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = stars(star)
print(star)
# for i in star:
#     print(i)