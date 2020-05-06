def f(n,k,m): #(순열의 n번 원소 결정)
    if n==k:
        print(p)
    else:
        for i in range(m):
            if used[i]==0:
                used[i] = 1
                p[n]=A[i]
                f(n+1,k,m)
                used[i] = 0




A=[0,1,2,3,4]
used = [0]*5
p=[0]*5
f(0,5,5)
## 1로 시작하는 조합만 만들고 싶으면?
# def f(n,k,m): #(순열의 n번 원소 결정)
#     if n==k:
#         print(p)
#     else:
#         for i in range(m):
#             if used[i]==0:
#                 used[i] = 1
#                 p[n]=A[i]
#                 f(n+1,k,m)
#                 used[i] = 0

# A=list(range(5))
# used = [0]*5
# p=[0]*5
# p[0]=1
# used[0]=1
# f(1,5,5)