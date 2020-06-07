T=int(input())
for tc in range(T):
    N,M = map(int,input().split())
    friend_list={i:[] for i in range(1,N+1)}
    for _ in range(M):
        a,b=map(int,input().split())
        friend_list[a].append(b)
        friend_list[b].append(a)
    # print(friend_list)
    if len(friend_list[1])==0:
        print(f'#{tc+1} {0}')
    else:
        res=[]
        for a in friend_list[1]:
            res.append(a)
            for k in friend_list[a]:
                if k not in res:
                    res.append(k)
        print(f'#{tc+1} {len(set(res))-1}')            