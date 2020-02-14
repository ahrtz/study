def f(n,k): # 변수는 전역변수처럼 쓴다 ex 여기선 리스트 A,B
    global maxV   # 외부에서 선언한 변수를 사용하려면(값을 변경하려면 )

    if n==k:
        # print(B)
        return

    else:
        # B[n] = A[n]
        if maxV <A[n]:
            maxV=A[n]
        # print(B)
        f(n+1,k)
        
    #return


# 재귀함수로 A배열을 B에 복사
A=[1,5,2]
B=[0]*3
maxV=0
f(0,len(A))
print(maxV)