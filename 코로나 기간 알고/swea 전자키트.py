from itertools import permutations
T=int(input())
for tc in range(T):
    g=int(input())
    pan=[]
    for _ in range(g):
        pan.append(list(map(int,input().split())))
    tmp=(permutations(list(range(g))))
    min_a=1000000000000000
    for route in tmp:
        tmp_sum=0
        for i in range(len(route)-1):
            tmp_sum+=pan[route[i]][route[i+1]]
            if tmp_sum>min_a:
                break
        tmp_sum+=pan[route[i+1]][route[0]]
        if tmp_sum<min_a:
            min_a=tmp_sum
    print(f"#{tc+1} {min_a}")