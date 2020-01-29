t= int(input())
for i in range(t):
    n=int(input())
    carrots = list(map(int,input().split()))
    cnt=1
    example=[0]*n
    for idx in range(0,len(carrots)-1):
        if carrots[idx]<carrots[idx+1]:
            cnt+=1 
            example[idx]=cnt
        else:
            cnt=1
            example[idx]=cnt
    print("#{} {}".format(i+1,max(example)))
