# # def f(n,k,m): #(순열의 n번 원소 결정)
# #     if n==k:
# #         print(p)
# #         # return p
# #     else:
# #         for i in range(m):
# #             if used[i]==0:
# #                 used[i] = 1
# #                 p[n]=A[i]
# #                 f(n+1,k,m)
# #                 used[i] = 0




# # A=[0,1,2,3,4]
# # used = [0]*5
# # p=[0]*5
# # f(0,5,5)
# # 1로 시작하는 조합만 만들고 싶으면?
# def f(n,k,m): #(순열의 n번 원소 결정)
#     if n==k:
#         # print(p)
#         tmp.append(p)
#     else:
#         for i in range(m):
#             if used[i]==0:
#                 used[i] = 1
#                 p[n]=A[i]
#                 f(n+1,k,m)
#                 used[i] = 0

# A=list(range(5))
# used = [0]*5
# tmp=[]
# p=[0]*5
# p[0]=0
# used[0]=0
# f(0,5,5)
# print(tmp)
def combi(lis,n):
    ret=[]
    if n>len(lis):
        return ret
    
    if n==1:
        for i in lis:
            ret.append([i])
    elif n>1:
        for i in range(len(lis)-n+1):
            for temp in combi(lis[i+1:],n-1):
                print(ret,i)
                ret.append([lis[i]]+temp)
    return ret

A=[0,2,4,8]
combi(A,3)
print(combi(A,3))