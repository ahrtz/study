T=int(input())
for tc in range(T):
    N,M = map(int,input().split()) # N 수열의 길이 M 수열의 개수
    
    temp=list(map(int,input().split()))
    
    for _ in range(M-1):
        num_list=list(map(int,input().split()))
        for i in range(len(temp)):
            if temp[i] > num_list[0]:
                temp[i:i] = num_list
                break
        else:
            temp = temp+num_list
    
    print("#{} {}".format(tc+1,' '.join(list(map(str,temp[::-1][:10])))))

