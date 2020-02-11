import pprint
T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    farm=[]
    for _ in range(N):
        tmp = list(map(int,input().split()))
        farm.append(tmp)
    diff=[]
    #
    # for row in range(1,N): # 선을 그을수있는 경우의수 계산
    #     for col in range(1,N):
    #         suma = 0  # 초기화
    #         sumb = 0
    #         sumc = 0
    #
    #         ## 왼쪽부분이 합쳐졋을때
    #         for rowa in range(0,N): # a
    #             for cola in range(col):
    #                 suma += farm[rowa][cola]
    #         for rowb in range(row): # b
    #             for colb in range(col,N):
    #                 sumb += farm[rowb][colb]
    #         for rowc in range(row,N):
    #             for colc in range(col,N):
    #                 sumc += farm[rowc][colc]
    #         diff.append(max(suma,sumb,sumc)-min(suma,sumb,sumc))
    # print(diff)
    for row in range(1,N):  # 선을 그을수있는 경우의수 계산
        for col in range(1, N):
            suma = 0  # 초기화
            sumb = 0
            sumc = 0

            ## 오른쪽부분이 합쳐졋을때
            for rowa in range(row):  # a
                for cola in range(col, N):
                    suma += farm[rowa][cola]
            for rowb in range(row):  # 요게 a
                for colb in range(col):
                    sumb += farm[rowb][colb]
            for rowc in range(row, N):
                for colc in range(0,N):
                    sumc += farm[rowc][colc]
            diff.append(max(suma, sumb, sumc) - min(suma, sumb, sumc))
        print(suma,sumb,sumc)
    print("#{} {}".format(tc+1, min(diff)))
