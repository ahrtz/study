T=int(input())
for tc in range(T):
    N= int(input())
    sosu_list=[]
    for i in range(2,N+1):
        cnt=0
        for j in range(1,i+1):
            if i % j == 0:
                cnt+=1
        if cnt == 2:
            sosu_list.append(i)
    # print(sosu_list)
    tmp=[]
    for so in sosu_list:
        if so < N:
            tmp.append(so)
    # print(tmp)
    count=0
    for n in range(len(tmp)):
        if tmp[n]<N//2:
            for m in range(n,len(tmp)):
                if tmp[m]<N//2:
                                    
                    for o in range(m,len(tmp)):
                        if tmp[n]+tmp[m]+tmp[o]==N:
                            count+=1
                        elif tmp[n]+tmp[m]+tmp[o]>N:
                            break
    print("#{} {}".format(tc+1,count))
