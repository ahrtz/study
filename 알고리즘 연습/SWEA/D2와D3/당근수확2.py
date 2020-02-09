T=int(input())
for tc in range(T):
    N,M = map(int,input().split()) # N 밭의 개수 M은 수레용량
    bat=list(map(int,input().split()))
    bat.insert(0,0)
    ep=sum(bat)
    i=1
    sure=0
    cnt=0
    while True:
        if ep < M:
            cnt = (len(bat)-1)*2
            break
        if bat[-1]==0 and sure !=0:
            cnt += (len(bat)-1)*2
            break
        if bat[-1]==0:
            break
        if bat[i]==0:
            i += 1
        elif bat[i]!=0:
            bat[i] -=1
            sure +=1
            if sure == M:
                cnt += 2*i
                sure = 0

    print("#{} {}".format(tc+1,cnt))

    
    

