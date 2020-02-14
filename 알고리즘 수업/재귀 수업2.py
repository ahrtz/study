def f(n,k,v):
    if n==k:
        return 0 #찾는 값이 배열에 없으면
    elif A[n]==v:
        return n
    else:
        
        return f(n+1,k,v) # 다음 원소를 확인하러 이동


A=[1,3,2,4,5,7,8,9]
print(f(0,len(A),5))