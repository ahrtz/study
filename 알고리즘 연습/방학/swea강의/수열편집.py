T=int(input())
for tc in range(T):
    n,m,l=map(int,input().split())
    num_list=list(map(int,input().split()))
    for _ in range(m):
        tmp=list(map(str,input().split()))
        if tmp[0]=='I':
            num_list.insert(int(tmp[1]),int(tmp[2]))
        elif tmp[0]=='D':
            num_list.pop(int(tmp[1]))
        else:
            num_list[int(tmp[1])]=int(tmp[2])
    
    if len(num_list)-1<l:
        print("#{} {}".format(tc+1,-1))
    else:
        print("#{} {}".format(tc+1,num_list[l]))
