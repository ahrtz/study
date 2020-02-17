def f(n,k):
    if n==k: # 부분집합1개완성
        for i in range(k):
            if L[i]==1:
                print(A[i],end=" ")
        print()
        return
    else:
        L[n] = 0
        print("?1")
        f(n+1,k)
        print("?2")
        L[n] = 1
        f(n+1,k)
        print("/")


A=[1,2,3,4]
L=[0]*4
f(0,4)
