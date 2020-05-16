
def track(pan,arr,n):
    global min_cnt
    if len(arr)==n:
        cnt=0
        for i in range(n):
            cnt+=pan[i][arr[i]]
        if cnt<min_cnt:
            min_cnt=cnt
        return
    else:
        if arr:
            cnt=0
            for i in range(len(arr)):
                cnt+=pan[i][arr[i]]
                if cnt>min_cnt:
                    return
        candid=list(range(n))
        for i in arr:
            candid.remove(i)
        if candid !=[]:
            for i in candid:
                arr.append(i)
                track(pan,arr,n)
                arr.pop()


T=int(input())
for tc in range(T):
    n=int(input())
    pan=[list(map(int,input().split())) for _ in range (n  )]

    min_cnt=100000000000

    for i in range(n):
        track(pan,[i],n)


    print(f"#{tc+1} {min_cnt}")
        