# arr='abc'
# N=len(arr)
# bit=[0]*N

# def subset(k,n):
#     if k==n:
#         print(bit)
#     else:
#         bit[k]=1
#         subset(k+1,n)
#         bit[k]=0
#         subset(k+1,n)
# subset(0,N)
arr='abc'
N=len(arr)
bit=[0]*N
A=[]
def subset(k,n,cnt):
    if k==n:
        print(cnt,len(A),A)
    else:
        A.append(arr[k])
        subset(k+1,n,cnt+1)
        A.pop()
        subset(k+1,n,cnt)
subset(0,N,0)