T=int(input())
for tc in range(T):
    N=int(input())
    num_list=list(map(int,input().split()))
    check=[0]*10001
    cnt = 1
    check[0]=1
    sum_num = [0]
    for i in range(N):
        for j in range(len(sum_num)):
            if check[sum_num[j]+num_list[i]]==0:
                check[sum_num[j]+num_list[i]]=1`
                sum_num.append(sum_num[j]+num_list[i])
                cnt+=1
                
    print(sorted(sum_num))
    print("#{} {}".format(tc+1,cnt))

