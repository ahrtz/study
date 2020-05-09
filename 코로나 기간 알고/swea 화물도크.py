T=int(input())
for tc in range(T):
    num = int(input())
    화물_리스트 = []
    for _ in range(num):
        화물_리스트.append(list(map(int,input().split())))
    화물_리스트=sorted(화물_리스트,key=lambda x: (abs(x[0]-x[1])))
    # print(화물_리스트)
    time=[0]*25
    cnt=0
    for i in range(len(화물_리스트)):
        a,b=화물_리스트[i][0],화물_리스트[i][1]
        if 1 in set(time[a:b]):
            continue
        else:
            # print(a,b,'%')
            for k in range(a,b):
                time[k]=1
            cnt+=1
    print(f'#{tc+1} {cnt}')
