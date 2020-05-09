T=int(input())
for tc in range(T):
    num = int(input())
    화물_리스트 = []
    for _ in range(num):
        화물_리스트.append(list(map(int,input().split())))
    화물_리스트=sorted(화물_리스트,key=lambda x: x[0])
    시간간격=[]
    print(화물_리스트)
    for i in range(len(화물_리스트)):
        시간간격.append(화물_리스트[i][1]-화물_리스트[i][0])
    total_time=24-화물_리스트[0][0]-(24-화물_리스트[-1][1])
    print(total_time,시간간격)
    cnt=len(시간간격)
    while sum(시간간격)>total_time:
        tmp=max(시간간격)
        시간간격.remove(tmp)
        cnt-=1
    # print(cnt)

    
    
