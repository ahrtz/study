# def track(pan,arr,n):
#     global min_cnt
#     if len(arr)==n:
#         # print(arr)
#         cnt=0
#         for i in range(n):
#             cnt+=pan[i][arr[i]]
#         if cnt<min_cnt:
#             min_cnt=cnt
#         return
#     else:
#         if arr:
#             cnt=0
#             for i in range(len(arr)):
#                 cnt+=pan[i][arr[i]]
#                 # print(arr,cnt,min_cnt)
#                 if cnt>min_cnt:
#                     return
#         candid=list(range(n))
#         # print(candid)
#         for i in arr:
#             candid.remove(i)
#         if candid !=[]:
#             for i in candid:
#                 # print(pan,'32',arr)
#                 arr.append(i)
#                 track(pan,arr,n)
#                 arr.pop()


from itertools import permutations
T=int(input())
for tc in range(T):
    n=int(input())
    pan=[list(map(int,input().split())) for _ in range (n  )]
    # 조합으로 쉽게 하는거
    a=list(range(n))
    num_list=permutations(a,len(a))
    min_cnt=100000000000
    
    for num in num_list:
        cnt=0
        # print(num)
        for i in range(len(num)):
            cnt+=pan[i][num[i]]
            if cnt>min_cnt:
                break
        if cnt<min_cnt:
            min_cnt=cnt
    # for i in range(n):
    #     track(pan,[i],n)


    print(f"#{tc+1} {min_cnt}")
        