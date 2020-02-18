T=int(input())
for tc in range(T):
    N,M = map(int,input().split())
    num_list=list(map(int,input().split()))
    for i in range(M):
        a=num_list.pop(0)
        num_list.append(a)
    print("#{} {}".format(tc+1,num_list[0]))