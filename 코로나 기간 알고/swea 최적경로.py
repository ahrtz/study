from itertools import permutations
T=int(input())
for tc in range(T):
    n=int(input())
    tmp_list=list(map(int,input().split()))
    sp =tmp_list[:2]
    home = tmp_list[2:4]
    tmp_list=tmp_list[4:]
    a=permutations(list(range(n)),n)
    min_sum = 10000000000
    for i in a:
        tmp_sum=0
        for k in range(len(tmp_list)//2):
            if k == 0:
                tmp_sum += abs(sp[0]-tmp_list[2*i[k]])+abs(sp[1]-tmp_list[2*i[k]+1])
                # print(tmp_sum,k)
            else:
                tmp_sum += abs(tmp_list[2*i[k-1]]-tmp_list[2*i[k]])+abs(tmp_list[2*i[k-1]+1]-tmp_list[2*i[k]+1])
                # print(tmp_sum,k)
        tmp_sum += abs(home[0]-tmp_list[i[-1]*2])+abs(home[1]-tmp_list[i[-1]*2+1])
        # print(i,tmp_sum)
        if tmp_sum<min_sum:
            min_sum=tmp_sum
    print(f"#{tc+1} {min_sum}")