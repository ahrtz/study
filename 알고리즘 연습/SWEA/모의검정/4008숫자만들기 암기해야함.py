# import itertools
# T=int(input())
# for tc in range(T):
#     N=int(input())
#     plus , minus , mul , div = map(int,input().split())
#     num_list= list(map(int,input().split()))
    
#     sign_list = ["+"]*plus + ["-"] * minus + ['*']*mul + ['/'] * div
#     print(sign_list)
#     sign_combi = list(set(itertools.permutations(sign_list,N-1)))
#     resu_list=[]

    
#     for k in range(len(sign_combi)):
#         tmp=num_list[0]    
#         i=0
#         while i<len(num_list)-1:
#             if sign_combi[k][i]=="+":
#                 tmp += num_list[i+1]
#                 i+=1
#             elif sign_combi[k][i]=="-":
#                 tmp -= num_list[i+1]
#                 i+=1
#             elif sign_combi[k][i]=="*":
#                 tmp *= num_list[i+1]
#                 i+=1
#             elif sign_combi[k][i]=="/":
#                 tmp = int(tmp/num_list[i+1])
#                 i+=1
#         resu_list.append(tmp)
    
#     print("#{} {}".format(tc+1,max(resu_list)-min(resu_list)))
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    
    def generat(chosen, used):
        
        # 2.
        if len(chosen) == r:
            a.append(chosen[:])
                        
            return a
	
        for i in range(len(arr)):
	    # 3.
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i] = 1
                
                generat(chosen, used)

                used[i] = 0
                chosen.pop()
        
    generat([], used)
T=int(input())
for tc in range(T):
    N=int(input())
    plus , minus , mul , div = map(int,input().split())
    num_list= list(map(int,input().split()))
    
    sign_list = ["+"]*plus + ["-"] * minus + ['*']*mul + ['/'] * div
    a=[]
    
    permutation(sign_list,N-1)
    print(a)
    sign_combi = a
    resu_list=[]

    
    # for k in range(len(sign_combi)):
    #     tmp=num_list[0]    
    #     i=0
    #     while i<len(num_list)-1:
    #         if sign_combi[k][i]=="+":
    #             tmp += num_list[i+1]
    #             i+=1
    #         elif sign_combi[k][i]=="-":
    #             tmp -= num_list[i+1]
    #             i+=1
    #         elif sign_combi[k][i]=="*":
    #             tmp *= num_list[i+1]
    #             i+=1
    #         elif sign_combi[k][i]=="/":
    #             tmp = int(tmp/num_list[i+1])
    #             i+=1
    #     resu_list.append(tmp)
    
    # print("#{} {}".format(tc+1,max(resu_list)-min(resu_list)))