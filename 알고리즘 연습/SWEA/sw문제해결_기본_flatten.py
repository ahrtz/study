
for i in range(10):
    trial = int(input())
    num_list = list(map(int,input().split()))
    cnt=0
    while cnt<trial:
        num_list[num_list.index(max(num_list))] =num_list[num_list.index(max(num_list))]-1 
        num_list[num_list.index(min(num_list))] =num_list[num_list.index(min(num_list))]-1
        cnt+=1
    print(max(num_list)-min(num_list))







    # ex=[]
    # for i in range(len(num_list)):
    #     a=num_list[i]-int(sum(num_list)/len(num_list))
    #     ex.append(abs(a))
    # avg=sum(num_list)/len(num_list)
    # if avg==int(avg):
    #     diff = 0
    # else:
    #     diff = 1
    # needtrial=sum(ex)/2
    # trial_diff=needtrial-trial
    # tot_diff = trial_diff / (len(num_list)/2)
    # result= math.ceil(tot_diff) * 2 + diff
    # print(result)