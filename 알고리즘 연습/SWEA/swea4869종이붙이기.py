# import itertools
# test=int(input())
# for i in range(test):
#     small=1
#     large=2
#     width=int(input())
#     width = int(width/10)
#     # print(width)
#     large_num = width//large
#     # print(large_num)
#     result_1=[]
#     #배열 만들기
#     for i in range(large_num+1):
#         result_2=[]
        
#         for ex1 in range(i):
#             result_2.append(2)

#         num_1 = width-2*i
#         numm=0
#         while numm<num_1:
#             result_2.append(1)
#             numm+=1
        
#         result_1.append(result_2)
#     # print(result_1)
#     #배열별 조합 만들기
#     combi_num=0
#     result_Set=[]
#     for combi in  result_1:
#         ex1=itertools.permutations(combi,len(combi))
#         result_Set.append(set(ex1))
#     # print(result_Set)
#     # # print(len(result_Set[2]))
#     # print(len(result_Set[-1]))
#     # print((result_Set[-1]))
#     # print(list(result_Set[2])[0].count(2))


#     ## 요소길이 측정 1보다 크면 2갯수 세서 갯수ㄱㅖ산 
#     # 아니면 바로 개수 계산 1만있으면 1이고 
#     # 2갯수 별로 3**N 개 -1 * len 
    
#     cnt=0
#     cnt += (3**(list(result_Set[-1])[0].count(2))-1) * len(result_Set[-1]) +1

#     # for sset in result_Set:
#     #     if len(sset)==1:
#     #         print(sset)
#     #         if list(sset)[0].count(2) != 0 :
#     #             cnt += (3**list(sset)[0].count(2))-1
                
#     #         else:
#     #             cnt += 1
            
#     print(cnt)
def GetSome(x):
    if x == N:
        return 1
    if x > N:
        return 0
    return GetSome(x+10) + GetSome(x+20) * 2


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    print('#{} {}'.format(tc, GetSome(0)))