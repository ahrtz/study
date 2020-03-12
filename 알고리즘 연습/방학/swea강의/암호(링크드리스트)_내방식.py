T= int(input())
for tc in range(T):
    N,M,K = map(int,input().split())
    num_list = list(map(int,input().split()))
    tmp=0
    
    for _ in range(K):
        tmp += (M)
        if tmp >len(num_list):
            tmp -= len(num_list)
            tmp_num=num_list[tmp-1]+num_list[tmp]
            num_list.insert(tmp,tmp_num)
        elif tmp == len(num_list):
            tmp_num=num_list[tmp-1]+num_list[0]
            num_list.insert(tmp+1,tmp_num)
        else:
            tmp_num=num_list[tmp-1]+num_list[tmp]
            num_list.insert(tmp,tmp_num)
    print("#{} {}".format(tc+1," ".join(repr(k) for k in num_list[::-1][:10])))
