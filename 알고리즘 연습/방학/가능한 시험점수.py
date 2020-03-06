T=int(input())
for tc in range(T):
    N=int(input())
    num_list=list(map(int,input().split()))
    max_num= sum(num_list)
    
    num_list=sorted(num_list,reverse=True)
    result = []
    check =[0]*(max_num+1)
    check[max_num]=1
    stack = [max_num]
    cnt = 1
    for i in range(N):
        for k in range(len(stack)):
            if check[stack[k]-num_list[i]]==0:
                check[stack[k]-num_list[i]]=1
                stack.append(stack[k]-num_list[i])
                cnt +=1
                    
                
    # print(i,result)
    # print(cnt)
    print("#{} {}".format(tc+1,cnt))

