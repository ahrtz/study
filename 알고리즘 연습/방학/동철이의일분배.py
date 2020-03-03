import itertools
T=int(input())
for tc in range(T):
    N=int(input())
    pro_pan=[list(map(int,input().split())) for _ in range(N)]
    combi_list=list(itertools.permutations(list(range(N)),N))
    # print(combi_list)
    maxx=0
    for combi in combi_list:
        cnt = 1
        for i in range(N):
            cnt *= pro_pan[i][combi[i]]
        if cnt > maxx:
            maxx = cnt
    maxx = maxx / (10**2)**N
    print("#{} {:0.6f}".format(tc+1,maxx*100))
