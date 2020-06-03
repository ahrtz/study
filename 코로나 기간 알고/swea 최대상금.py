def search(n):
    global max_num
    if n==time:# n 번 돈거 전부다 체크하기 
        if max_num<int("".join(numlist)):
            max_num=int("".join(numlist))
    else:
        for i in range(len(numlist)-1):
            for j in range(i+1,len(numlist)):
                numlist[i],numlist[j]=numlist[j],numlist[i]
                tmp=int(''.join(numlist))
                if tmp not in res[n]: # 이미 바꿧던게 존재하면 안돌리기 
                    res[n].append(tmp)
                    search(n+1)
                numlist[i],numlist[j]=numlist[j],numlist[i]
                



T=int(input())
for tc in range(T):
    numlist,time = input().split()
    numlist = list(numlist)
    time = int(time)
    res=[[]for _ in range(time)]
    max_num=0
    search(0)
    print(f'#{tc+1} {max_num}')
