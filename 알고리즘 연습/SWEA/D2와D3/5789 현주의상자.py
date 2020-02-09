T=int(input())
for tc in range(T):
    N,Q = map(int,input().split())
    box = [0]*N
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for k in range(L,R+1):
            box[k-1]=i
    print("#{} {}".format(tc+1," ".join(str(m) for m in box)))