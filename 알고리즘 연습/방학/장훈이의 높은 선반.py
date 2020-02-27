import itertools
T=int(input())
for tc in range(T):
    N,B =map(int,input().split())
    ki_list = list(map(int,input().split()))
    S = sum(ki_list)
    if B==S:
        print("#{} {}".format(tc+1,0))
    else:
        result=[]
        for i in range(len(ki_list)):
            combi_list = list(itertools.combinations(ki_list,len(ki_list)-i))
            # print(combi_list)
            for k in combi_list:
                # print(k)
                # print(sum(k))
                if sum(k)>=B:
                    result.append(sum(k))
        
        result.sort()

        print("#{} {}".format(tc+1,result[0]-B))