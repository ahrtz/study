def f(n,k): #(순열의 n번 원소 결정)
    if n==k:
        print(p)
    else:
        for i in range(k):
            if used[i]==0:
                used[i] = 1
                p[n]=A[i]
                f(n+1,k)
                used[i] = 0




A=[1,2,3]
used = [0]*3
p=[0]*3
f(0,3)