# 합이 10인 경우의 수...
def f(n,k,su): # n은 원소의 인덱스  (포함여부를 검토할 원소의 인덱스),k 배열의 크기 su 는 n-1 까지 고려한 부분집합의 합
    global cnt,ans
    cnt+=1
    if n==k:
        if su==55:
            ans+=1
        print(su)
    # elif su>55:
    #     return
    else:
        
        f(n+1,k,su) # n 번 원소가 포함되지 않은 부분집합의 합
        f(n+1,k,su+A[n]) # n번 원소가 포함된 부분집합의 합
         





A=[1,2,3,4,5,6,7,8,9,10] # 일때 부분집합 만들기 
# L = [0]*10
ans=0
cnt=0
f(0,10,0)
print(ans,cnt)