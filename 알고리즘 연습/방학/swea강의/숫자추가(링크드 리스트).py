T=int(input())
for tc in range(T):
    N,M,L = map(int,input().split())
    num_list=list(map(int,input().split()))
    for _ in range(M):
        idx , val = map(int,input().split())
        num_list.insert(idx,val)
    print("#{} {}".format(tc+1,num_list[L]))