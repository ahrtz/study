def f(n,k): #(순열의 n번 원소 결정)
    global result
    if n==k:
        print(p)
        result.append(p)
    else:
        for i in range(k):
            if used[i]==0:
                used[i] = 1
                p[n]=A[i]
                f(n+1,k)
                used[i] = 0



result = []
A=[1,2,3,4,5]
used = [0]*5
p=[0]*5
f(0,5)
print(result)