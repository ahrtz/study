T=int(input())
for tc in range(T):
    N,K = map(int,input().split()) # 숫자 갯수  k 는  오름차순 시 10 번째 
    num_list = list(map(str,input()))
    set_list = []
    temp=N//4
    for _ in range(N//4):
        set_list.append("".join(num_list[0:temp]))
        set_list.append("".join(num_list[temp:temp*2]))
        set_list.append("".join(num_list[temp*2:temp*3]))
        set_list.append("".join(num_list[temp*3:temp*4]))
        a=num_list.pop()
        num_list.insert(0,a)
    set_list=list(set(set_list))
    num_dic = {'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15}
    final = []

    for i in set_list:
        temp_num=0
        for k in range(temp):
            if i[k].isdigit():
                temp_num += (16**(temp-(k+1)))*int(i[k])
            else:
                temp_num += (16**(temp-(k+1)))*num_dic[i[k]]
        final.append(temp_num)
    # print(set_list)
    # print(final)
    final = sorted(final,reverse=True)
    print("#{} {}".format(tc+1,final[K-1]))