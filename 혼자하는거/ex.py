T=int(input())
for tc in range(T):
    bar=list()
    tmp=int(input())
    for _ in range(tmp):
    	a,b = map(int,(input().split()))
    	bar.append((a,b))
    cnt=0
    for k in range(len(bar)-1):
        for j in range(k+1,len(bar)):
            sx,sy=bar[k]
            ex,ey=bar[j]
            if sx<ex and sy>ey:
                cnt+=1
    print(f"#{tc+1} {cnt}")