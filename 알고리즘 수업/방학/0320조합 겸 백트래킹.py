arr = 'abx' 
N= len(arr)
order=[]

visit=[0]*N
def perm(k,n):
    if k==n:
        print(order)
    else:
        for i in range(N):
            if visit[i]:continue
            visit[i] = 1
            order.append(arr[i])
            perm(k+1,n)
            visit[i]=0
            order.pop()
perm(0,N)