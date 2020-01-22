a= int(input())
for i in range(a):
    res=[]
    length=int(input())
    num_list=list(map(int,input().split()))
    while len(num_list)!=0:
        num_list = sorted(num_list,reverse=False)
        res.append(num_list.pop())
        num_list = sorted(num_list,reverse=True)
        res.append(num_list.pop())
    res=res[:10]
    result = " ".join(repr(k) for k in res)
    print("#{} {}".format(i+1,result))